from pomegranate import *
D1 = DiscreteDistribution({'True':0.6, 'False': 0.4})
D2 = DiscreteDistribution({'True':0.011, 'False': 0.989})
D3 = DiscreteDistribution({'True':0.00852, 'False': 0.99148})
D4 = DiscreteDistribution({'True':0.014, 'False': 0.986})
D5 = DiscreteDistribution({'True':0.00065, 'False': 0.989})
D6 = DiscreteDistribution({'True':0.48, 'False': 0.52})
D7 = DiscreteDistribution({'True':0.95, 'False': 0.05})
D8 = DiscreteDistribution({'True':0.107, 'False': 0.893})
D9 = DiscreteDistribution({'True':0.3, 'False': 0.7})

S11 = ConditionalProbabilityTable(
    [['True', 'True', 0.91],
     ['True', 'False', 0.09],
     ['False', 'True', 0.18],
     ['False', 'False', 0.82]], [D1]
    )
SH = ConditionalProbabilityTable(
    [['True', 'True','True','True', 0.33],
     ['True', 'True','True','False', 0.67],    
     ['True', 'True','False','True', 0.22],
     ['True', 'True','False','False', 0.78],     
     ['True', 'False','True','True', 0.11],
     ['True', 'False','True','False', 0.89],     
     ['True', 'False','False','True', 0.22],
     ['True', 'False','False','False', 0.78],     
     ['False', 'True','True','True', 0.22],
     ['False', 'True','True','False', 0.78],     
     ['False', 'True','False','True', 0.11],     
     ['False', 'True','False','False', 0.89],     
     ['False', 'False','True','True', 0.11],
     ['False', 'False','True','False', 0.89],     
     ['False', 'False','False','True', 0.01],
     ['False', 'False','False','False', 0.99]], [D1,D2,D3]
    )
S31 = ConditionalProbabilityTable(
    [['True', 'True', 0.93],
     ['True', 'False', 0.07],
     ['False', 'True', 0.02],
     ['False', 'False', 0.98]], [D3]
    )
S32 = ConditionalProbabilityTable(
    [['True', 'True', 0.82],
     ['True', 'False', 0.18],
     ['False', 'True', 0.14],
     ['False', 'False', 0.86]], [D3]
    )
S41 = ConditionalProbabilityTable(
    [['True', 'True', 0.75],
     ['True', 'False', 0.25],
     ['False', 'True', 0.67],
     ['False', 'False', 0.33]], [D4]
    )
SL = ConditionalProbabilityTable(
    [['True', 'True','True', 0.22],
     ['True', 'True','False', 0.78],
     ['True', 'False','True', 0.11],
     ['True', 'False','False', 0.89],
     ['False', 'True','True', 0.78],
     ['False', 'True','False', 0.22],
     ['False', 'False','True', 0.89],
     ['False', 'False','False', 0.11]], [D4,D5]
    ) 
S51 = ConditionalProbabilityTable(
    [['True', 'True', 0.86],
     ['True', 'False', 0.14],
     ['False', 'True', 0.32],
     ['False', 'False', 0.68]], [D5]
    )
SB = ConditionalProbabilityTable(
    [['True', 'True','True', 0.89],
     ['True', 'True','False', 0.11],     
     ['True', 'False','True', 0.45],
     ['True', 'False','False', 0.55],     
     ['False', 'True','True', 0.47],
     ['False', 'True','False', 0.53],    
     ['False', 'False','True', 0.06],
     ['False', 'False','False', 0.94]], [D6,D7]
    )  
S71 = ConditionalProbabilityTable(
    [['True', 'True', 0.91],
     ['True', 'False', 0.09],
     ['False', 'True', 0.54],
     ['False', 'False', 0.46]], [D7]
    )
S81 = ConditionalProbabilityTable(
    [['True', 'True', 0.98],
     ['True', 'False', 0.02],
     ['False', 'True', 0.17],
     ['False', 'False', 0.83]], [D8]
    )
SC = ConditionalProbabilityTable(
    [['True', 'True','True','True','True', 0.44],
     ['True', 'True','True','True','False', 0.56],     
     ['True', 'True','True','False','True', 0.33],
     ['True', 'True','True','False','False', 0.67],     
     ['True', 'True','False','True','True', 0.33],
     ['True', 'True','False','True','False', 0.67],     
     ['True', 'True','False','False','True', 0.22],
     ['True', 'True','False','False','False', 0.78],
     ['True', 'False','True','True','True', 0.33],
     ['True', 'False','True','True','False', 0.67],
     ['True', 'False','True','False','True', 0.22],
     ['True', 'False','True','False','False', 0.78],   
     ['True', 'False','False','True','True', 0.22],
     ['True', 'False','False','True','False', 0.78],
     ['True', 'False','False','False','True', 0.11],
     ['True', 'False','False','False','False', 0.89],
     ['False', 'True','True','True','True', 0.33],     
     ['False', 'True','True','True','False', 0.67],  
     ['False', 'True','True','False','True', 0.22],   
     ['False', 'True','True','False','False', 0.78],
     ['False', 'True','False','True','True', 0.22],  
     ['False', 'True','False','True','False', 0.78], 
     ['False', 'True','False','False','True', 0.11],
     ['False', 'True','False','False','False', 0.89],
     ['False', 'False','True','True','True', 0.22],
     ['False', 'False','True','True','False', 0.78],
     ['False', 'False','True','False','True', 0.11],
     ['False', 'False','True','False','False', 0.89],
     ['False', 'False','False','True','True', 0.11],   
     ['False', 'False','False','True','False', 0.89],
     ['False', 'False','False','False','True', 0.01],
     ['False', 'False','False','False','False', 0.99]], [D6,D7,D8,D9]
    ) 
S91 = ConditionalProbabilityTable(
    [['True', 'True', 0.91],
     ['True', 'False', 0.09],
     ['False', 'True', 0.21],
     ['False', 'False', 0.79]], [D9]
    )

s001 = State(D1, name = 'Acute myocardial infarction')
s002 = State(D2, name = 'Pericarditis')
s003 = State(D3, name = 'Heart failure')
s004 = State(D4, name = 'Pneumonia')
s005 = State(D5, name = 'Pulmonary embolism')
s006 = State(D6, name = 'Chest wall pain')
s007 = State(D7, name = 'Gastroesophageal reflux disease')
s008 = State(D8, name = 'Panic disorder/ anxiety state')
s009 = State(D9, name = 'Acute thoracic aortic dissection')

s1 = State(S11, name = 'chest pain radiates to both arms')
s2 = State(SH, name = 'chest pain in heart')
s3 = State(S31, name = 'history of heart failure')
s4 = State(S32, name = 'history of acute myocardial infarction')
s5 = State(S41, name = 'fever')
s6 = State(SL, name = 'chest pain in lung')
s7 = State(S51, name = 'localized muscle tension and pain reproducible by palpation')
s8 = State(SB, name = 'burning retrosternal pain')
s9 = State(S71, name = 'sour or bitter taste in the mouth')
s10 = State(S81, name = 'had an anxiety attack in the past 4 weeks')
s11 = State(SC, name = 'middle chest pain')
s12 = State(S91, name = 'back pain and a pulse differential in the upper extremities')

network = BayesianNetwork('Chest Pain Classification')
network.add_nodes(s001,s002,s003,s004,s005,s006,s007,s008,s009,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12)
network.add_edge(s001, s1)
network.add_edge(s001, s2)
network.add_edge(s002, s2)
network.add_edge(s003, s2)
network.add_edge(s003, s3)
network.add_edge(s003, s4)
network.add_edge(s004, s5)
network.add_edge(s004, s6)
network.add_edge(s005, s6)
network.add_edge(s005, s7)
network.add_edge(s006, s8)
network.add_edge(s006, s11)
network.add_edge(s007, s8)
network.add_edge(s007, s9)
network.add_edge(s007, s11)
network.add_edge(s008, s10)
network.add_edge(s008, s11)
network.add_edge(s009, s11)
network.add_edge(s009, s12)
network.bake()

        
def patient_interview():
    symptoms_list = ['chest pain radiates to both arms'
                     ,'chest pain in heart'
                     ,'history of heart failure'
                     ,'history of acute myocardial infarction'
                     ,'fever'
                     ,'chest pain in lung'
                     ,'localized muscle tension and pain reproducible by palpation'
                     ,'burning retrosternal pain'
                     ,'sour or bitter taste in the mouth'
                     ,'had an anxiety attack in the past 4 weeks'
                     ,'middle chest pain'
                     ,'back pain and a pulse differential in the upper extremities']
    observations = {}

    for symptom in symptoms_list:
        ans = input('Do you have a ' + symptom + ':')
        if ans == 'yes':
            observations[symptom]= 'True'
        elif ans == 'no':
            observations[symptom]= 'False'

    beliefs = network.predict_proba(observations)
    for state, belief in zip(network.states, beliefs):
        if not isinstance(belief, str) :
            print( state.name,': probability = ',
                  belief.probability('True'))

patient_interview()
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    