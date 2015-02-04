#!/usr/bin/perl
  #
  # The traditional first program.

  # Strict and warnings are recommended.
  use strict;
  use warnings;
  use List::Tuples qw(:all);
  use Data::Dumper;
  
if (@ARGV) {
    my %TODOexists;
    my $databaseEntryRE = qr/(\d+)( .+)/; #This regex will check if a database entry is of the right form, which for now is "(Line number) (message)"
    my @databaseOfTODOs;
    my $TODOre = qr/TODO\:(.+)/;
    
foreach my $arg (@ARGV) {
    open(my $fh, "<" , $arg) or die "cannot open < $arg \n"; #### Firstly we scan through any previous TODOs and hash the task so as to not double print
    print "Looking in file: " . $arg . " \n";
    
    if (-e "TODOs" . $arg) {
        open(my $save ,"<","TODOs" . $arg);
          print "Looking at previous TODO list:  " . "TODOs" . $arg. "\n";
        while (my $line = <$save>){
            
            if ($line =~ $databaseEntryRE) {
                
                push(@databaseOfTODOs, [$1,$2]);
            }
            
            $TODOexists{$line} = 1;
           
        }
        close $save;
        
    }
    
    
    open(my $out ,">","TODOs" . $arg) or die "can't open outfile for $arg \n";
    
    
    
    
    while (my $line = <$fh>) {
        my $linenum = $. ;
        my $string = '';
        
        ($string = $linenum . "$1\n" )if ($line =~  $TODOre );
        
        unless (exists $TODOexists{$string} or $string eq '') { ###### Here we check if this is a previously stored TODO, and ignore it if so. the string eq '' condition is there
            push(@databaseOfTODOs, [$1,$2]) if $string =~ $databaseEntryRE ;
        } 
        
    }
    
    

    @databaseOfTODOs = sort { $a->[0] <=> $b->[0] } @databaseOfTODOs;

    foreach (@databaseOfTODOs){
       print $out "$_->[0]$_->[1]\n";
    }
    
    close($out)|| warn "close failed \n";
    print "Leaving file: $arg \n";
    close ($fh) || warn "close failed \n";
}

} else {
    print "You must provide a file to extract TODO's from. \n"
}
