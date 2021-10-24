all: time_naive.svg time_total.svg time_improved.svg solutions.svg least_numbers.svg \
     time_naive.png time_total.png time_improved.png solutions.png least_numbers.png

time_%.csv: %.py bench.py
	python3 -B bench.py $* > $@

time_%.svg: time_%.csv time_plot.py
	python3 -B time_plot.py -f svg $<

time_%.png: time_%.csv time_plot.py
	python3 -B time_plot.py -f png $<

solutions.%: s.py
	python3 -B s.py -f $*

least_numbers.%: n.py
	python3 -B n.py -f $*
