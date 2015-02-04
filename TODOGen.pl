#!/usr/bin/perl
  #
  # The traditional first program.

  # Strict and warnings are recommended.
  use strict;
  use warnings;
if (@ARGV) {
    

foreach my $arg (@ARGV) {
    open(my $fh, "<" , $arg) or die "cannot open < $arg \n";
    print $arg . "\n";
    
    
    open(my $out ,">>","TODOS:" . $arg) or die "can't open outfile for $arg \n";
    
    while (my $line = <$fh>) {
        my $linenum = $. ; 
        print $out $linenum . "$1\n" if ($line =~ /\%TODO\:(.+)/ );
        
    }
    
    
    
    
    close($out)|| warn "close failed \n";
    close ($fh) || warn "close failed \n";
}

} else {
    print "You must provide a file to extract TODO's from. \n"
}
