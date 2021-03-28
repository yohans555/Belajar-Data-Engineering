soal nomor 1

class Movie():
    kategori_movie ='dewasa' #class attribute
    def __init__(self,judul,rating,tahun_rilis): #intance attribute
        self.judul=judul
        self.rating=rating
        self.tahun_rilis=tahun_rilis
    
    def durasi(self,waktu=None): #instance method dan overloading
        if waktu==none :
            print(self.judul,'mempunyai durasi yang tidak diketahui')
        else:
            print(self.judul,'mempunyai durasi',waktu,'menit')
    @classmethod #class method
    def kategori(cls):
        print('film ini memiliki kategori',Movie.kategori_movie)

class animasi(Movie): #inheritance
    kategori_movie= 'anak anak' #overriding
    def(self):
        print(f)


soal nomor 2

find: Provides a feature rich and granular search capability to look for files and directories.
locate: Provides a fast database-driven search for programs and commands.
which: Searches the $PATH looking for executable files
whereis: Searches the $PATH looking for executable files, man pages, and source code files.
whatis: Searches the man one-line descriptions for matches to the search term.
apropos: Searches the man page with more fidelity than whatis, for matches to the search term or terms.

soal nomor 3 

grep:
The grep filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern. 
The pattern that is searched in the file is referred to as the regular expression (grep stands for globally search for regular expression and print out). 

syntax : grep [options] pattern [files]

ack :
Ack searches the named input FILEs (or standard input if no files are named, or the file name - is given) for lines containing a match to the given PATTERN . By default, ack prints the matching lines.
Ack can also list files that would be searched, without actually searching them, to let you take advantage of ack's file-type filtering capabilities.

syntax :ack [options] PATTERN [FILE...]