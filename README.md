# Various Production Pieces
This houses snippets of code that is needed in a production setting. I include bite-sized examples on how to appropriately address specific components that need to be included in a mature codebase.

Logging is incredibly useful when documenting potential errors, exceptions, notes, locations, etc of various lines of code. This is especially useful when you do not have print statements or a console readably available for debugging purposes. Whenever something may crash, the go-to is an error file. How does this error file even get populated? Check out the example on logging in python. Logging is associated with the YouTube video: [**Logging Link**](https://youtu.be/mJm3YFzJBcA)

Absolute paths are incredibly underrated. Everyone should know proper procedures when it comes to sourcing local dependencies. Being consistent is the most important aspect. Although there is a preference for absolute paths over relative paths, you can go either way. But, more often than not, I see absolute paths being used more in a production environment. [**Absolute Paths**](https://youtu.be/4Dbn2p0Mcqc)
