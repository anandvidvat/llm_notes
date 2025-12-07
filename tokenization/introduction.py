# author : Anand Vidvat Arza
# create date : Dec, 07, 2025
# last update date  : Dec, 07, 2025

def intro_to_tokenization():
  process = """ Tokenization step in LLM training and inference process is a crutial first step towards model development.
  it can be summarized as the process of converting Raw Text (usually a string class implementation in various programming langauges) (input or otherwise) which is generated represted as Unicode Strings (alphabets, numerics, non-english characters and emojis etc) 
  into a vector of numbers (integers, floating points f16, f32 etc.)
  """
  token_desc = """ the output of the above tokenization step are called tokens, or each number is called a token """
  
  usage_step = """ For LLMs development, we need a procedure which can be invoked to encode (string* to tokens) or decode (tokens to string*) """
  
  vocab_size = """ the vocabulary size of an LLM is the number of unique tokens it can encode. 
                In this case, higher the number of vocab size, more the distinct pieces of information can be encoded into tokens.
                this is a good trait of a LLM """

