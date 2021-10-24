watch: site
	./site watch

build: site
	./site build

site: site.hs
	ghc-8.6.5 --version
	ghc-8.6.5 --make -v -dynamic site

clean:
	rm ./site
	rm -rf _cache
	rm -rf _site/
