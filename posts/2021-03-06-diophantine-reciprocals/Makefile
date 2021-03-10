all: time_naive.svg time_total.svg time_improved.svg \
     time_naive.png time_total.png time_improved.png

time_%.csv: %.py bench.py
	python3 -B bench.py $* > $@

time_%.svg: time_%.csv time_plot.py
	python3 -B time_plot.py -f svg $<

time_%.png: time_%.csv time_plot.py
	python3 -B time_plot.py -f png $<