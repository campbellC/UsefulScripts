#!/usr/bin/perl
  #
  # The traditional first program.

  # Strict and warnings are recommended.
  use strict;
  use warnings;
if (@ARGV) {
    my %database;

foreach my $arg (@ARGV) {
    open(my $fh, "<" , $arg) or die "cannot open < $arg \n"; #### Firstly we scan through any previous TODOs and hash the task so as to not double print
    print "Looking in file: " . $arg . " \n";
    
    if (-e "TODOs" . $arg) {
        open(my $save ,"<","TODOs" . $arg);
          
        while (my $line = <$save>){
            
           $database{$line} = 1;
           
        }
        close $save;
        
    }
    
    open(my $out ,">>","TODOs" . $arg) or die "can't open outfile for $arg \n";
    
    
    
    
    while (my $line = <$fh>) {
        my $linenum = $. ;
        my $string = '';
        
        ($string = $linenum . "$1\n" )if ($line =~ /TODO\:(.+)/ );
        
        unless (exists $database{$string} or $string eq '') { ###### Here we check if this is a previously stored TODO, and ignore it if so. the string eq '' condition is there
            print $out $string;            # in order avoid an uninitialised variable issue.
        } 
        
    }
    
    
    
    
    close($out)|| warn "close failed \n";
    print "Leaving file: $arg \n";
    close ($fh) || warn "close failed \n";
}

} else {
    print "You must provide a file to extract TODO's from. \n"
}
