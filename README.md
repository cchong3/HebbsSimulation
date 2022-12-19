# HebbsSimulation

## Crystal Chong & Emilie Grand'Pierre

Cognitive Architecture, CSCI 3400 / DCS 3400

### Background 

As computer science majors, the difference between human learning and computer learning is one of the biggest takeaways from this course. Throughout our many semesters of AI courses, the ideas of optimization, balancing greediness and randomness, and Bayesian reasoning contrast the core ways we, as humans, learn. Our unit of thought, the cell assembly, is a product of our perception and enables us to make predictions even when things are uncertain. Individual pieces of knowledge and experience come together to build a prototype that can be called on when needed. Thus, for humans, learning is the building and changing of our internal structures using recruitment and fractionation to fine-tune our cell assembly. At the heart of learning is Hebb’s rule which is the idea of wiring neurons that fire together. Another cornerstone of building cell assemblies is the compensatory learning model: in a cell-assembly, connections that have never proven to be useful are weakened. When paired together, over time these two concepts allow our connections strengthen within a given cell assembly, and we can perform closure for an object or abstract idea based on experience. 

Using cell assemblies, humans can learn a wide array of concepts when compared to the hyper-specialized computer systems present in our world today. Through this final project, we hoped to highlight the elegance and coherence of our cognitive architecture by embedding some of the core ideas of learning explored in the semester into a model to help visualize how this process occurs in humans. Personally, math is something that has never come easily. Calculus, especially, is a form of logic that I still cannot fully wrap my head around, but its applications are incredibly vast: just when I think I am done seeing the purpose of the derivative, it rears its complicated head. When thinking back on my years of math education, this continued confusion despite repeated exposure to Calculus can be thought of as ‘gaps’ in my cell assembly. When compared to an expert’s cell assembly, my prototype of math fails to properly link ideas: solving calculus problems requires me to take large leaps because my cell assembly does not accurately model the steps needed. Stemming from this continued confusion, we thought to model the varying cell assemblies that can result from different iterations of learning. 

### How the Code Works 

In this model, we explore how one’s environment, prior knowledge, and time affects the resulting cell assembly. We follow the idea that if any human is placed in a supportive environment, eventually one can build a prototype that enables one to solve calculus problems. This process, however, may take varied amount of time based on prior experience. We deduced that Calculus can be broken up into 5 key ideas: Algebra 1, Geometry, Algebra 2, Precalculus, and Calculus itself. These core ideas generalize the typical math curriculum of the United States and follows the schematic nature of cell assemblies: one cannot understand precalculus without first understanding algebra and geometry. Accordingly, we encoded that one cannot move on to the next core idea of calculus without first understanding the previous one. 

Our system works by gathering how long a user can spend learning calculus and their prior knowledge. This semester underscored the importance of a supportive environment when learning, so we also ask the learning environment of the user. If the environment is supportive, then the rate of learning is higher when compared to learning in an unsupportive environment. Regardless of whether the environment is supportive or unsupportive, the learning rate will be lower if it is paired with a confusion score indicated by the user. The system also adjusts its learning rate based on whether the user is a satisficer or maximizer. Maximizers have a higher threshold for proceeding to the next topic, and is rewarded an extra 0.05 to their learning rate given a more comprehensive understanding of the prevous core course. Our model focuses on the recruiting process of learning and the building of associations. If a user only has 5 days to cram before an exam and is only confident in math up to geometry, no matter how supportive the environment, it is hard to believe that the user’s cell assembly of math will be capable of passing the test. To use, simply run cell_assembly.py and follow the prompts of the system. The generated output is a graph that models our prediction of what a user’s cell assembly will be based on the information provided. 

In further work, it would be beneficial to encode how higher mastery at lower levels effects the resulting cell assembly. In other words, our system fails to currently represent how spending more time fully understanding algebra 1 and 2 beyond the threshold value can lead to one learning and understanding later concepts faster. Finally, it would be interesting to see how one’s cell assembly of math translates to other related fields like physics or music. In reality, learning is associative beyond a single subject. A more complete model of cell assemblies would show how experts in one field are able to transfer components of one cell assembly to make predictions and inferences about another subject.  

