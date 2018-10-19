s=input ("Give me a verb")
if len(s)>=3 and s[-3:]!="ing":
    print ("%sing"%(s))
elif (s[-3:]>="ing"):
    print ("%sly"%(s))
else:
    print ("%s" % (s))
