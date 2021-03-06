#!/usr/bin/env python3
import time

import numpy as np

from data_ingestion.ingest_points import init_dataframe
from analysis import stat as a


def main(gender: str, stat: str, normalization: str, reverse: bool, limit: int, verbose=False):
  FILE_NAME = f'charting-{gender}-points.csv'
  NUM_ROWS = None # charting-m-points has 297532 lines # A value of None will get them all
  start_time = time.time()

  # ingest
  df_points = init_dataframe(FILE_NAME, NUM_ROWS)
  if verbose:
    print('data loaded.')
    print(' Elapsed time = {}'.format(time.time() - start_time))
    print('crunching numbers...')

  # analyze
  df_players = a.player_to_stats_df(df_points)
  player_rank_list = a.player_to_stat(df_players, stat, normalization, reverse, limit, verbose)

  # outgest (convert to output data structure for frontend)
  frontend_player_rank_list = [{'category': player, 'value': score} for player,score in player_rank_list]

  # output
  if verbose:
    print('analysis finished')
    print(' Elapsed time = {}'.format(time.time() - start_time))
  return frontend_player_rank_list

if __name__ == '__main__':
  stat = 'dblFault'
  pr = main(gender='m', stat=stat, normalization='percent', reverse=False, limit=3, verbose=True)
  print(f'\n\nstat:{stat}. ranking:\n', pr, '\n')
  print('Finished crunching numbers.', end='')

