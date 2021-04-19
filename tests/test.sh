#!/bin/bash
echo "Testing preprocessing with rules..."

Compare_Outputs() {
if cmp -s $1 $2
then
   echo "Test Passed!"
else
   echo "Test Failed!"
   exit 1
fi
}

echo "Test 1: Basic with POS Tag"

input_text="US forces in Iraq need to get their act together there and really dampen the situation and stop inflaming things by confrontational policies."
rule_file="rule-set.ppr"
expected_output="US forces in Iraq need to sort out their issues there and really dampen the situation and stop inflaming things by confrontational policies ."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 2: Multiple rules"

input_text="US forces in Iraq need to get their act together there and the vice president should feel free to jump in"
rule_file="rule-set.ppr"
expected_output="US forces in Iraq need to sort out their issues there and the vice president should not hesitate to get involved"

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 3: Optional Token"

input_text="You are a student here, aren't you?"
rule_file="rule-set.ppr"
expected_output="You are a student here , right ?"

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

input_text="We aren't going with him, are we?"
rule_file="rule-set.ppr"
expected_output="We are n't going with him , right ?"

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

input_text="He really looks like that actor, does he not?"
rule_file="rule-set.ppr"
expected_output="He really looks like that actor , right ?"

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 4: Multiple variables"

input_text="She dislikes the lazy and will fix this department."
rule_file="rule-set.ppr"
expected_output="She dislikes lazy people and will fix this department ."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 5: OR Operator"

input_text="He told me to give police the slip and then I told them to give her the slip."
rule_file="rule-set.ppr"
expected_output="He told me to evade police and then I told them to evade her ."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 6: NOT Operator"

input_text="She dislikes the lazy employees and will fix this department."
rule_file="rule-set.ppr"
expected_output="She dislikes the lazy employees and will fix this department."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 7: Match Any Token Operator"

input_text="It's the one with the actor who went to jail."
rule_file="rule-set.ppr"
expected_output="It 's the one which has the actor who went to jail ."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 8: Mappings in Replacement Rules"

input_text="This pandemic is a thorn in his side."
rule_file="rule-set.ppr"
expected_output="This pandemic is a persistent problem for him ."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

input_text="This pandemic is a thorn in their side."
rule_file="rule-set.ppr"
expected_output="This pandemic is a persistent problem for them ."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

input_text="This pandemic is a thorn in Pushpa's side."
rule_file="rule-set.ppr"
expected_output="This pandemic is a persistent problem for Pushpa ."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

input_text="This pandemic is a thorn in the police's side."
rule_file="rule-set.ppr"
expected_output="This pandemic is a persistent problem for the police ."

python3 ../src/preprocess.py "$input_text" "rulesets/$rule_file" > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

rm -rf check_output.txt temp_output.txt

echo "All tests successfully passed!"


