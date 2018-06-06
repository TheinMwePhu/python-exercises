formatter+"%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("One","two","three","four")
print formatter %(True,False,True, False)
print formatter %(formatter,formatter,formatter,formatter)
print formatter.format("Try you","Own text here"."May be  a poen","Or a song about fear")
