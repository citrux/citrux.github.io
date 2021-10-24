watch: site
	./site watch

build: site
	./site build

site: site.hs
	whereis ghc
	whereis ghc-8.6.5
	ghc-8.6.5 --make -v -dynamic site

clean:
	rm ./site
	rm -rf _cache
	rm -rf _site/
