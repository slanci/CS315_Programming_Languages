use Data::Dumper qw(Dumper);
print "-----------\n";
# question 1
my @names =("Sila","Oguz");
print($names[1]);
print "\n";
my %ages= ('Sila' => '20', 'Oguz' => '29', 'Feriha' => '38');
print "Sila's age: ", $ages{'Sila'}, "\n";
print "Oguz's age: ", $ages{'Oguz'}, "\n";
print "Feriha's age: ", $ages{'Feriha'}, "\n";
print "-----------\n";
# question 2
print "Perl range checking error message.\n";
print "-----------\n";
my @rangeArr = ("me", "you","her", "him");
my @slice = $rangeArr[7];
print "@slice\n";
print "-----------\n";
# question 3 & 4 & 5
print "Ragged Array\n";
my @raggedArr = ([1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]); #ragged array created
print "@$_\n" for @raggedArr;
print "-----------\n";
# question 6
$multDimArr[2][3][4][5] = 7;
$multDimArr[1][1][1][1] = 7;
print Dumper \@multDimArr;
print "-----------\n";
# question 7
my @stuff = ("book","pencil", "ruler","paper");
foreach(@stuff){
	print "$_\n";
}
print "-----------\n";
# question 8
my @part = @stuff[1,2];
print "@part\n";
print "-----------\n";