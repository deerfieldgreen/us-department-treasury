import pandas as pd
import os
from github import Github, GithubException
import base64
import datetime
import pytz
from udt.utils import *
import dotenv
import pickle

dotenv.load_dotenv()

import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_and_encode_file(file_path, encode=True):
    """Read the file content and encode it in base64."""
    with open(file_path, 'rb') as file:
        content = file.read()
    if encode:
        return base64.b64encode(content).decode('utf-8')
    else:
        return content


def save_and_update_github(file_path, repo, github_path):
    """Save file to GitHub and update if it already exists."""
    content = read_and_encode_file(file_path, encode=False)
    try:
        git_file = repo.get_contents(github_path)
        logger.info(f"Found existing file: {git_file.path}")
        repo.update_file(
            git_file.path,
            f"Updated file for {datetime.datetime.now(pytz.timezone('US/Eastern')).date()}",
            content,
            git_file.sha,
        )
    except Exception as e:
        if isinstance(e, GithubException) and e.status == 404:  # File not found
            logger.info(f"File not found. Creating a new file: {github_path}")
            repo.create_file(
                github_path,
                f"Created file for {datetime.datetime.now(pytz.timezone('US/Eastern')).date()}",
                content,
            )
        else:
            logger.error(f"An error occurred: {str(e)}")
            raise e


if __name__ == '__main__':
    # 1. Fetch and save daily treasury rates data for current year
    timezone = pytz.timezone('US/Eastern')
    current_time = datetime.datetime.now(timezone)
    current_year = current_time.year
    url = f'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value={current_year}'
    dfs = pd.read_html(url)

    df = dfs[0]
    work_dir = os.getcwd()
    csv_path = os.path.join(work_dir, 'data', f'{current_year}-daily-treasury-rates.csv')
    pickle_path = os.path.join(work_dir, 'data', f'{current_year}-daily-treasury-rates.pkl')
    csv_dir = os.path.dirname(csv_path)

    rel_cols = [x for x in df.columns if 'Yr' in x or 'Mo' in x or 'Date' in x]
    df = df[rel_cols]

    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df.sort_values('Date', inplace=True, ascending=False)
    
    # Save as CSV
    df.to_csv(csv_path, index=False)
    
    # Save as pickle
    with open(pickle_path, 'wb') as f:
        pickle.dump(df, f)

    # 2. Merge all the years into one file
    file_names = sort_file_names(csv_dir)
    merged = merge_files(file_names, csv_dir)
    all_years_csv_path = os.path.join(csv_dir, 'daily-treasury-rates.csv')
    all_years_pickle_path = os.path.join(csv_dir, 'daily-treasury-rates.pkl')

    # Save merged data as CSV and pickle
    merged.to_csv(all_years_csv_path, index=False)
    with open(all_years_pickle_path, 'wb') as f:
        pickle.dump(merged, f)

    # Prepare github
    token = os.environ.get("GIT_TOKEN")
    g = Github(token)
    repo = g.get_repo(
        "deerfieldgreen/us-department-treasury"
    )  # Replace with your repo details

    # Update or create files on GitHub
    save_and_update_github(all_years_csv_path, repo, "data/daily-treasury-rates.csv")
    save_and_update_github(all_years_pickle_path, repo, "data/daily-treasury-rates.pkl")
    save_and_update_github(csv_path, repo, f"data/{current_year}-daily-treasury-rates.csv")
    save_and_update_github(pickle_path, repo, f"data/{current_year}-daily-treasury-rates.pkl")

    logger.info(f"All files pushed to Github")