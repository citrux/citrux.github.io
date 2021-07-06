--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
import           Data.Monoid            (mappend)
import           Data.List              (isInfixOf)
import           Hakyll
import           System.FilePath.Posix  (splitFileName)


htmlCompiler :: Compiler (Item String)
htmlCompiler = do
    path <- getResourceFilePath
    let (dir,_) = splitFileName path
    getResourceString >>= withItemBody (unixFilter "asciidoctor-latex"
                                                  ["-b"
                                                  , "html5"
                                                  , "-B"
                                                  , dir
                                                  , "-s"
                                                  , "-a"
                                                  , "embedded"
                                                  , "-a"
                                                  , "skip-front-matter"
                                                  , "-"])


--------------------------------------------------------------------------------
-- Replace url of the form foo/bar/index.html by foo/bar.
removeIndexHtml :: Item String -> Compiler (Item String)
removeIndexHtml item = return $ fmap (withUrls removeIndexStr) item
    where
        removeIndexStr :: String -> String
        removeIndexStr url = case splitFileName url of
                                (dir, "index.html") | isLocal dir -> dir
                                _                                 -> url
        isLocal :: String -> Bool
        isLocal uri        = not (isInfixOf "://" uri)


--------------------------------------------------------------------------------
main :: IO ()
main = hakyll $ do
    match "images/*" $ do
        route   idRoute
        compile copyFileCompiler

    match "css/*" $ do
        route   idRoute
        compile compressCssCompiler

    match "posts/*/index.adoc" $ do
        route $ setExtension "html"
        compile $ htmlCompiler
            >>= loadAndApplyTemplate "templates/post.html"    postCtx
            >>= loadAndApplyTemplate "templates/default.html" postCtx
            >>= relativizeUrls
            >>= removeIndexHtml

    match "posts/**/*" $ do
        route   idRoute
        compile copyFileCompiler

    -- create ["archive.html"] $ do
    --     route idRoute
    --     compile $ do
    --         posts <- recentFirst =<< loadAll "posts/*"
    --         let archiveCtx =
    --                 listField "posts" postCtx (return posts) `mappend`
    --                 constField "title" "Archives"            `mappend`
    --                 defaultContext

    --         makeItem ""
    --             >>= loadAndApplyTemplate "templates/archive.html" archiveCtx
    --             >>= loadAndApplyTemplate "templates/default.html" archiveCtx
    --             >>= relativizeUrls


    match "index.html" $ do
        route idRoute
        compile $ do
            posts <- recentFirst =<< loadAll "posts/*/index.adoc"
            let indexCtx =
                    listField "posts" postCtx (return posts) `mappend`
                    defaultContext

            getResourceBody
                >>= applyAsTemplate indexCtx
                >>= loadAndApplyTemplate "templates/default.html" indexCtx
                >>= relativizeUrls
                >>= removeIndexHtml

    match "templates/*" $ compile templateBodyCompiler


--------------------------------------------------------------------------------
postCtx :: Context String
postCtx =
    dateField "published" "%d.%m.%Y" `mappend`
    modificationTimeField "updated" "%d.%m.%Y" `mappend`
    defaultContext

