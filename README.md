Following is the supplementary material for the article ["Foundations of Prescriptive Process Monitoring"] by [Irene Teinemaa](https://scholar.google.nl/citations?user=UQZ22uQAAAAJ&hl=en&oi=ao), [Niek Tax](https://scholar.google.com.au/citations?user=XkRvCC4AAAAJ&hl=en&oi=ao), [Massimiliano de Leoni](http://www.win.tue.nl/~mdeleoni/), [Marlon Dumas](http://kodu.ut.ee/~dumas/), and [Fabrizio Maria Maggi](https://scholar.google.nl/citations?user=Jo9fNKEAAAAJ&hl=en&oi=sra) that is currently under submission at the [16th International Conference on Business Process Management](http://bpm2018.web.cse.unsw.edu.au/)

The code provided in this repository implements the techniques for alarm-based prescriptive process monitoring.
 Furthermore, the repository provides an implementation of the experimental setus and can be used to investigate:
 * The effect of different cost models on the benefit of an alarm-based prescriptive process monitoring system.
 * The effect of different alarming strategies on the performance of the alarm-based prescriptive process monitoring system.
 * The effect of different probabilistic classification algorithms on the performance of the alarm-based prescriptive process monitorring system.

The scripts trains a [Long Short Term Memory (LSTM)](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)-based predictive model using the data about historical, i.e. completed process instances. Next, the models are evaluated on running, i.e. incomplete instances.

**Requirements:**   
Python 3. Additionally, the following Python libraries are required to run the code: _sklearn_,_hyperopt_, _numpy_.  

**USAGE:**  
**Data format**   
The tool assumes the input is a complete log of all traces in the CSV format wherein the first column is a case ID, then activity name or ID and finally the activity timestamp. Then, this input log is temporally split in 64% of the data for training the classifier, 16% of the data to optimize the alarming strategy, and 20% for evaluation. On the evaluation set the tool evaluates the obtained reduction in the cost of processing a trace using the alarming system, given a particular cost model. We provide sample datasets, including those used in the paper, in the _data_ folder.

**Model training:**   
`python train.py`    
This script trains a two-layer LSTM model with one shared layer on one of the data files in the data folder of this repository (by default, on the [_helpdesk_ event log](https://data.mendeley.com/datasets/39bp3vv62t/1)). To change the input file to another one from the data folder, indicate its name in line 46. It is recommended to run this script on GPU, as recurrent networks are quite computationally intensive. 

**Evaluation:**  
`python evaluate_next_activity_and_time.py`   
This script takes as input the LSTM or RNN weights found by `train.py` and predicts the next event and its relative timestep for a partial trace. Change the path in line 176 of this script to point to the h5 file with LSTM or RNN weights generated by train.py. As an example, we provide the file _model_89-1.50.h5_ with one of the trained models

`python evaluate_suffix_and_remaining_time.py`   
This script predicts the continuation of a partial trace, i.e. its suffix, until its completion.

`python calculate_accuracy_on_next_event.py`.
This script evaluates the performance of the next event prediction (not the whole suffix). It takes the output of `evaluate_suffix_and_remaining_time.py` as input, therefore, the latter needs to be executed first

**Reference:**
If you use the code from this repository, please cite the original paper:
```
@article{Teinemaa2018,
  title={Foundations of Prescriptive Process Monitoring },
  author={Teinemaa, Irene and Tax, Niek and de Leoni, Massimiliano and Dumas, Marlon and Maggi, Fabrizio Maria},
  journal={arXiv},
  year={2018}
}
```
