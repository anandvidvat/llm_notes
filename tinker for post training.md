

Thinking Labs which was founded by Mira Takur (ex- CTO of OpenAI),
released a python package called [tinker](https://thinkingmachines.ai/blog/announcing-tinker/)

In the pipeline of LLM training, testing, optimizing, serving;  my initial impressions from the announment is that this package is relevant to the "post-training" phase of LLM development & usage process.

To brief, LLM training can be broken down into two distinct steps
  1. pre-training
  2. post-training

Pre-training Phase : 
  pre-training phase involves feed the model, which has billions of params but lacks any meaningful context within its weights is just a skeleton at this point, 
  with huge amount of the data, this kind of training process can be unsupervised.
  
  the essential point of this step to bring the model capability to predict the next possible token given a sequence of input tokens 
  i.e example such a sentence construction given initial starting x phrases, given x1 x2 x3 x4... model predicts x5..x6 and x7
  
  more intitutive example : 
                input : The quick brown fox jumps .. 
                model predicts : over the lazy dog
                forming the final sentence  : The quick brown fox jumps over the lazy dog
  example at gemini : https://g.co/gemini/share/0673d97c0917
  
  the supposed theory is that with enough pre-training data corpus, the model with num of billions of params can scale well 
  and give raise to "emergent behavior", which means, it can perform reasonably well on tasks it is not been previously exposed. 

Post Training Phase :
  post training phase is for fine-tuning a model for a specific task or action to be performed by the pre-training LLM. this is helpful process to get better results out of the LLMs 
  rather than using naive/vanilla foundational model as research shows considerable performance gains when a model is fine-tuned on a specific task

  So how does post-training process differ?
  Among many approachs, Reinformant Learning (RL) methodology has proven to meaningful in fine-tuning the LLMs to align with desired behaviour. 
  The LLM acts as the Agent which interacts with the world & produces an output given an input, for the desired output the model is rewarded and (for unknown behaviour it is peanilized?
  there are various RL methods which can be used to fine-tune a model. 
  
  To Quote the annnouncment of Tinker by Thinking Labs, "Tinker is a managed service that runs on our internal clusters 
  and training infrastructure. We handle scheduling, resource allocation, and failure recovery. 
  This allows you to get small or large runs started immediately, without worrying about managing infrastructure. 
  We use LoRA so that we can share the same pool of compute between multiple training runs, lowering costs."

  The above snippet reveals that Tinker uses Low Rank Adaptation Methodology to fine-tune the LLM models.
  as of this writing, the models supported by Thinking labs are Qwen and Llama 

  Additionally, there is a (tinker-cookbook) [https://github.com/thinking-machines-lab/tinker-cookbook] package (by Thinking Labs) which is 
  builds on top of tinker APIs and another layer of abstraction to work with the open source models.
  
  

  

