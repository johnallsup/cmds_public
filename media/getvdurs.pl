#!/usr/bin/perl

@s = ();
%f = ();
$total = 0;
sub tohms {
  my ($t) = @_;
  my ($d,$h,$m,$s);
  $s = $t % 60;
  $m = int($t / 60) % 60;
  $h = int($t / 3600) % 24;
  $d = int($t / (3600*24));
  my ($x);
  $x = "";
  if( $d ) { $x .= "${d}d";}
  if( $h ) { $x .= "${h}h";}
  if( $m ) { $x .= "${m}m";}
  if( $s ) { $x .= "${s}";}
  if( $x =~ /^$/ ) { $x = "0"; }
  return $x;
}
for $file(@ARGV) {
  open(PIPE,"ffprobe '$file' 2>&1 |");
  @a = <PIPE>;
  close PIPE;
  for(@a) {
    if(/Duration:(.*),/) {
      $_ = $1;
      s/,.*$//;
			s/\..*//;
      @hms = split /:/;
      $t = 3600*int($hms[0]) + 60*int($hms[1]) + int($hms[2]);
      print "$file: $t ".(tohms($t))."\n";
      $total += $t;
      last;
    }
  }
}
if((scalar @ARGV) > 1) {
  print "Total: $total ".(tohms($total))."\n";
}
