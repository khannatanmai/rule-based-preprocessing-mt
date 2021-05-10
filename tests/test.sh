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

echo "US forces in Iraq need to get their act together there and really dampen the situation and stop inflaming things by confrontational policies." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="US forces in Iraq need to sort out their issues there and really dampen the situation and stop inflaming things by confrontational policies."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 2: Multiple rules"

echo "US forces in Iraq need to get their act together there and the vice president should feel free to jump in" > input_text.txt
rule_file="eng-hin.ppr"
expected_output="US forces in Iraq need to sort out their issues there and the vice president should not hesitate to get involved"

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 3: Optional Token"

echo "You are a student here, aren't you?" > input_text.txt
rule_file="eng-hin.ppr"
expected_output="You are a student here, right ?"

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "We aren't going with him, are we?" > input_text.txt
rule_file="eng-hin.ppr"
expected_output="We aren't going with him, right ?"

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "He really looks like that actor, does he not?" > input_text.txt
rule_file="eng-hin.ppr"
expected_output="He really looks like that actor, right ?"

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 4: Multiple variables"

echo "She made her students take the test again." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="She caused her students to take the test again."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 5: OR Operator"

echo "He told me to give police the slip and then I told them to give her the slip." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="He told me to escape from police and then I told them to escape from her."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 6: NOT Operator"

echo "She dislikes the lazy employees and will fix this department." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="She dislikes the lazy employees and will fix this department."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 7: Match Any Token Operator"

echo "It's the one with the actor who went to jail." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="It's the one which has the actor who went to jail."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 8: Mappings in Replacement Rules"

echo "This pandemic is a thorn in his side." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="This pandemic is a persistent problem for him."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "This pandemic is a thorn in their side." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="This pandemic is a persistent problem for them."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "This pandemic is a thorn in John's side." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="This pandemic is a persistent problem for John."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "This pandemic is a thorn in the police's side." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="This pandemic is a persistent problem for the police."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Test 9: Lemma matching"

echo "I will find this poster before I kick the bucket." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="I will find this poster before I die."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "Have you heard? The old man down the street has kicked the bucket." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="Have you heard? The old man down the street has died."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "He knew that he will be able to achieve everything on the list before he kicks the bucket." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="He knew that he will be able to achieve everything on the list before he dies."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

echo "He knew that he will be able to achieve everything on the list before kicking the bucket." > input_text.txt
rule_file="eng-hin.ppr"
expected_output="He knew that he will be able to achieve everything on the list before dying."

python3 ../src/preprocess.py "rulesets/$rule_file" input_text.txt > temp_output.txt
echo $expected_output > check_output.txt

Compare_Outputs check_output.txt temp_output.txt

rm -rf check_output.txt temp_output.txt input_text.txt

echo "All tests successfully passed!"


