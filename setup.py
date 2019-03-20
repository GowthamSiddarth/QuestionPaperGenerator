from distutils.core import setup

setup(
    name='QuestionPaperGenerator',
    version='0.0.1',
    packages=['questionpapergenerator', 'questionpapergenerator.util', 'questionpapergenerator.helper',
              'questionpapergenerator.models'],
    url='https://github.com/GowthamSiddarth/QuestionPaperGenerator.git',
    license='MIT',
    author='Gowtham Behara',
    author_email='gothsiddu@gmail.com',
    description='A practice Python Repository which generates a question paper based on marks distribution, questions '
                'and difficulty given'
)
