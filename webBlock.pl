#!/usr/bin/perl 


  # Strict and warnings are recommended.
  use strict;
  use warnings;
  use List::Tuples qw(:all);
  my $webSite = qr/(www\..+\..+)/; #checks if this is a webSite "www.WEBSITE.BLA"
  my $webSiteWithoutWWW = qr/[^\.]+\.[^\.]+/; #lets us write "WEBSITE.BLA" and not worry about www.
  my $hostsEntry = qr/127\.0\.0\.1 (www\..+\..+)/; #This regex will check if this is an entry of the form "127.0.0.1 www.WEBSITE.BLA"
  my $hostsFile = '/etc/hosts'; #This is the file which stores local hosts and may only work on OS X

sub siteIsInHosts{
	my $answer = 0;
	open(my $hosts, "<", $hostsFile) or die "cannot open hosts file \n";

	while(my $line = <$hosts>){
			if ( $line =~ $hostsEntry) {
				if ($1 eq $_[0]) {
						$answer = 1;
				}
		}
	}	
	close($hosts) || warn "close Failed\n";
	return $answer;
}


if (@ARGV) {
   my $blockFlag = 1; #true if we are blocking, false if we are unblocking
      foreach my $arg (@ARGV) {
		if ($arg eq "-u"){
			$blockFlag = 0;
			next;
		}
	if ($arg =~ $webSiteWithoutWWW){
		$arg = "www.". $arg;
	}
	if ($arg =~ $webSite) {
		if ($blockFlag) {
			print "Blocking " . $arg . "\n";
			if (siteIsInHosts($arg)){
				print $arg . " is already blocked\n";
				next;
			} else {
				open (my $hosts, ">>", $hostsFile) or die "cannot open hosts file";
 				print $hosts "127.0.0.1 " . $arg . "\n";
				print $arg . " is now blocked.\n";
				close($hosts) || warn "close Failed \n";		
			}
		} else {
		if (siteIsInHosts($arg)){
				print "Unblocking " . $arg . "\n";
				open (my $hosts, "<", $hostsFile) or die "cannot open hosts file";
				my @file = <$hosts>;
				close($hosts) || warn "close Failed \n";		
				@file = grep(!/127\.0\.0\.1 $arg/, @file);
				open ($hosts, ">", $hostsFile) or die "cannot open hosts file";
				print $hosts @file;
				close($hosts) || warn "close Failed \n";		
				print $arg . " is now unblocked.\n";
		} else {
				print $arg . " is not currently blocked\n";
				next;
	}
}
} else {
			
			print $arg . " is not a recognised webSite. Must be www.WEBSITE.BLA\n";
	}
	}
	    

	} else {
	    print "You must provide webSites to block or unblock. \n";
    	    print "Usage: webBlock [list of sites to block] -u [list of sites to unblock] \n";
}