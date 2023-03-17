import tpplex
import subprocess
import os, fnmatch

def execute_test(input_file):
    path_file = 'tests/' + input_file
    process = subprocess.Popen(['python', 'tpplex.py', path_file],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout, stderr

    output_file = open(path_file + ".out", "r")

    #read whole file to a string
    expected_output = output_file.read()

    output_file.close()

    print(stdout)
    print(expected_output)

    return stdout.decode("utf-8") == expected_output


#def teste_001():
#    assert execute_test("teste-001.tpp") == True

#def teste_002():
#    assert execute_test("teste-002.tpp") == True

#def teste_003():
#    assert execute_test("teste-003.tpp") == True

def testes():
    for file in fnmatch.filter(os.listdir('tests'), '*.tpp'):
        assert execute_test(file) == True
