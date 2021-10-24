watch: site
	./site watch

build: site
	./site build

site: site.hs
	ghc --make -dynamic site

clean:
	rm ./site
	rm -rf _cache
	rm -rf _site/
