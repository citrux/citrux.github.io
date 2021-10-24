watch: site
	./site watch

build: site
	./site build

site: site.hs
	/usr/bin/ghc --make -dynamic site

clean:
	rm ./site
	rm -rf _cache
	rm -rf _site/
