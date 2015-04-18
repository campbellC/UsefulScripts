#!/usr/bin/perl
#This script writes to a file dependencyTree.txt a list of the directories given to it, with the dependencies inside these
#it does this by looking for #include "DIR/HEADERFILE.h". It ignores self-dependency. It assumes you are in a directory storing each of these directories
  use strict;
  use warnings;
  use List::MoreUtils qw(uniq);
if (@ARGV) {
	my $outfile ='dependencyTree.txt';
	open(my $out ,">", $outfile) or die "can't open outfile for $outfile \n";
	my $includeRE = qr/\#include \"([^\/]+)\/.+\"/;
	foreach my $arg (@ARGV) {
		   my @dependencies;
		   
		   print $out "$arg:\n";
		   opendir(MYDIR,$arg);
		   my @files = grep(/\.h$|\.cpp$/,readdir(MYDIR));
		   foreach my $file (@files){
			open(my $fh, "<" , "$arg/$file") or die "cannot open  $file \n"; #
			print "Looking in file: " . $file . " \n";
			while(my $line = <$fh>){
				push(@dependencies, $1)	if ($line =~ $includeRE);
		}
		
	    
    
    
    
    
    print "Leaving file: $file \n";
    close ($fh) || warn "close failed \n";
    }
    @dependencies = uniq @dependencies;
    @dependencies = grep(!/^$arg$/,@dependencies);
		foreach (@dependencies){
				print $out "\t$_\n"
		}	
		
    print $out "\n";
	
}
     close($out)|| warn "close failed \n";
     closedir MYDIR;

} else {
    print "You have not provided any folders to build the dependency tree of\n"
}
