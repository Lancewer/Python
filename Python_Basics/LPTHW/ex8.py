__author__ = 'Lancewer'

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.", "That you could type up right", "But it didn't sing", "So I said goodnight.")

#compare %r and %s %s can correctly handle shift characters, but %r don't
print formatter % ("\na", '\tb', '\\ts','\ad')
other = "%s %s %s %s"
print other % ("\na", '\tb', '\\t','\ad')

