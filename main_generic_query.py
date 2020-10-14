#!/usr/bin/env python3
import time

import numpy as np

from data_ingestion.ingest_points import init_dataframe
from analysis import stat as a


def main(stat: str, limit: int, verbose=False):
	FILE_PATH = './data/charting-m-points.csv'
	NUM_ROWS = None # charting-m-points has 297532 lines # A value of None will get them all
	start_time = time.time()

	# ingest
	df = init_dataframe(FILE_PATH, NUM_ROWS)
	if verbose:
		print('data loaded.')
		print(' Elapsed time = {}'.format(time.time() - start_time))
		print('crunching numbers...')

	# analyze
	player_rank_list = a.player_to_stat(df, stat, limit)

	# outgest (convert to output data structure for frontend)
	frontend_player_rank_list = [{'category': player, 'value': score} for player,score in player_rank_list]

	# output
	if verbose:
		print('analysis finished')
		print(' Elapsed time = {}'.format(time.time() - start_time))
	return frontend_player_rank_list

if __name__ == '__main__':
	stat = 'double-faults'
	pr = main(stat=stat, limit=3, verbose=True)
	print(f'stat:{stat} player rank:', pr)
	print('Finished crunching numbers.', end='')

