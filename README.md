# Moon+ Reader Bookmarks Converter

This is a script to convert Moon+ Reader Bookmarks and notes into markdown.

The Markdown is copied to the system clipboard via the `pyperclip` module.

The Markdown can be saved to an output file.

# Requirements

The copy to system clipboard feature relies on the `pyperclip` python module.

Install `pyperclip`:

```
$ sudo pip install pyperclip
```

# Usage

Export your Moon+ Reader bookmarks to a text file and transfer them to your computer.

I install a simple text editor like QuickEdit Text Editor for Android.

In Moon+ Reader go to the Bookmarks for a book and tap the Share button at the bottom. Then tap "Share notes & highlights(TXT)".

From the Share menu I then select the text editor (QuickEdit). In QuickEdit I save the file into a folder that is synced by a cloud service.
I use a sync tool like Dropbox to automatically sync the files to my computer.

To copy the markdown to your system clipboard:

```
$ convert.py -i <filename>
```

If you want to output the markdown to a file:

```
$ convert.py -i <filename> -o <outputfilename.md>
```

# `pyperclip` Notes for Linux

`pyperclip` uses `xsel` or `xclip`, so make sure you have either of these tools installed on your distro.
