# Define a bunch of fun variables
H = "H"  # The letter H, duh
e = "e"  # The letter e, pretty straightforward
l1 = "l"  # l, but not the same as l2
l2 = "l"  # another l
o = "o"  # o, the 15th letter of the alphabet
comma = ","  # a comma, useful for pausing
_ = " "  # a space, because we need whitespace
W = "W"  # W, the 23rd letter
o2 = "o"  # same as o, but different variable
r = "r"  # the letter r
l3 = "l"  # l again, because 3 is a magic number
d = "d"  # d, not b or p, but d
exclamation_mark = "!"  # not a question
newline = "\n"  # because print doesn't work that way

# Redefine the sys module, because who needs the original?
class sys:
  # Redefine stdout, because encapsulation is overrated
  class stdout:
    # Redefine write, because we can
    class write:
      # init is like a constructor, but not really
      def __init__(self, *a, **kwa):
        # Print is easy, but we can make it easier
        print(*a, **kwa)

  # Make a "write" instance, because we need an instance
  stdout_write = stdout.write

  # Make stdout.write a property, just for kicks
  @property
  def stdout(self):
    return type("stdout", (), {"write": self.stdout_write})

# get an instance of the redefined sys module
sys = sys()

# Now we can "write" our Hello World message
# We need sep="" to avoid extra spaces, because we didn't use f-strings
# We need end="" to avoid an extra newline, because print is weird
getattr(sys.stdout, "write")(H+e+l1+l2+o+comma+_+W+o2+r+l3+d+exclamation_mark+newline, *(("",)*1), **{"end":""})
