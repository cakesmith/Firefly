Firefly
=======

##Firefly computing system

*To use this software, you must have `python3` and `tkinter` installed.*
### On Debian Linux derivatives:
```sh
sudo apt-get install python3 python3tk
python3 Jarvis.py
```


- `Ultron.py` is the high level language compiler (High level language -> VM intermediate format).
- `VirtualMachine.py` is the virtual machine translator (VM commands -> Assembly commands).
- `Jarvis.py` is the assembler and CPU simulator (Assembly commands -> binary).

The test code and some skeleton files are provided by the book [*The Elements of Computing Systems*](http://nand2tetris.org) by Noam Nisan and Shimon Schocken (MIT Press).

## Directory Structure
#### `tecs`
The `tecs` directory contains all of the source code included with the [book](http://nand2tetris.org).

#### `OS`
The `OS` directory contains the operating system files. The files ending in .jack are the high level language code, including:

- `Array.jack`
  * Create new arrays with `var myArray = Array.new(size)` and destroy them with `myArray.destroy()`.

- `Keyboard.jack`
  * `keyPressed()` Returns an ASCII code of the current key being pressed.
  * `readChar()` Reads the next character from the keyboard, waits until a key is pressed and then released, echoes the key to the screen, and returns the value of the pressed key.
  * `readLine(String message)` Prints a `message` on the screen, reads the next line of input until a newline character, and returns its value.
  * `readInt(String message)` Prints a `message` on the screen, reads the next line of input until a newline character, and returns its value as an integer, until the first non numeric character. 

- `Math.jack`
  * `twoToThe(x)` Returns 2^`x`.
  * `abs(x)` Returns the absolute value of ``x.
  * `multiply(x, y)` Returns the product of `x` and `y`.
  * `bit(x, j)` Returns `true` of the `j`-th bit of `x` is `1` and `false` otherwise.
  * `divide(x, y)` Returns the integer part of `x/y`. Returns `0` if `y > x`. Returns `-1` for overflow.
  * `xor(x, y)` Returns `x` XOR `y`.
  * `sqrt(x)` Returns the square root of `x`.
  * `max(x, y)` Returns the greater number of `x` and `y`.
  * `min(x, y)` Returns the smaller number of `x` and `y`.
  * `mod(n, base)` Returns the remainder of the division of `n` / `base`

- `Memory.jack`
  * `peek(address)` Returns the value of memory at location `address`.
  * `poke(address, value)` Sets the value of memory location `address` to `value`.
  * `alloc(size)` Allocates a block of memory of size `size` and returns a reference to its base address.
  * `deAlloc(object)` De-allocates a given object and frees its space.

- `Output.jack`
  * `moveCursor(i, j)` Moves the cursor to the `j`th column of the `i`th row.
  * `print(String s)` Prints an anonymous `String` and then destroys it.
  * `printLoc()` Prints the location of the cursor to the screen
  * `printChar(c)` Prints `c` at the cursor location and advances the cursor one column forward.
  * `printString(s)` Prints `s` starting at the cursor location and advances the cursor appropriately.
  * `printInt(i)` Prints the `Integer` `i` at the cursor location and advances the cursor appropriately.
  * `println()` Advances the cursor to the beginning of the next line.
  * `backSpace()` Moves the cursor one column back.

- `String.jack`
  * `new(maxLength)` Constructs a new `String` of maximum length `maxLength`. 
  * `myString.dispose()` Disposes this string and frees its space.
  * `myString.length()` Returns the length of this `String`.
  * `myString.charAt(j)` Returns the character at location j. If j < 0, counts from the end of the string backwards to j.
  * `myString.setCharAt(j, c)` Sets the `j`th character of this string to be `c`.
  * `myString.appendChar(c)` Appends the character `c` to the end of this `String`.
  * `myString.slice(from, to)` Returns a slice of this `String`.
  * `myString.grow(n)` Grows this string by `n` characters.
  * `myString.eraseLastChar()` Erases the last character in this `String`.
  * `myString.intValue()` Returns the integer value of this string until the first non-numeric character.
  * `myString.setInt(n)` Sets this string to hold a representation of the given number `n`.
  * `newLine()` Returns the newline character.
  * `backSpace()` Returns the backspace character.
  * `doubleQuote()` Returns the double quote character.

- `Sys.jack`
  * `init()` This method is called automatically upon bootstrapping, initializing all `.init()` methods of all other classes in the OS.
  * `halt()` Halts the execution of the processor, hopefully without catching anything on fire.
  * `wait(duration)` Waits approximately `duration` milliseconds and then returns.
  * `error(code)` Prints out the given error code and then halts.
  * `breakpoint()` An empty function to be used to inject breakpoints while debugging.

Also, this directory will contain `Main.jack` which houses the `main()` method, which is the beginning point of any application defined code.


