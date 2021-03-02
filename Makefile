watch: site
	./site watch

build: site
	./site build

site: site.hs
	ghc -dynamic --make site

clean:
	rm -rf _cache

