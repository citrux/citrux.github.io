all: time_naive.csv time_total.csv time_improved.csv

time_%.csv: %.py bench.py
	@ export PYTHONDONTWRITEBYTECODE=1
	python3 bench.py $* > $@
