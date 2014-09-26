import numpy as np
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib import rc 

def json_no_unicode(data):
    ''' 
    Decode a JSON file into strings instead of unicodes.
    Usage: json.loads(data, object_hook=json_no_unicode)
    '''
    if isinstance(data, dict):
        return {json_no_unicode(key): json_no_unicode(value) for key, value in data.iteritems()}
    elif isinstance(data, list):
        return [json_no_unicode(element) for element in data]
    elif isinstance(data, unicode):
        return data.encode('utf-8')
    else:
        return data


class crossing:
    def __init_(self,x,y,index):
        self.x=x
        self.y=y
        self.index=index
        
    def get_unitary(self):
        return np.matrix([[0,1],[1,0]])
        
    def draw(self, axis, text=True):
        ''' draw the crossing '''
        shape1x=np.array([0, 0.2, 0.8, 1])
        shape1y=np.array([0, 0, 1, 1])
        shape2x=np.array([0, 0.2, 0.4, 0.4, 0.6, 0.8, 1])
        shape2y=np.array([1, 1, 0.666, 0.333, 0.333, 0, 0])
        t=.2
        axis.plot(shape1x+self.x, shape1y+self.y, 'k-')
        axis.plot(shape2x+self.x, shape2y+self.y, 'k-')
        if text:
            color='#880000'
            axis.text(self.x+.5, self.y+.2, 'C%d' % self.index, color=color, fontsize=5, ha='center', va='bottom')
        
    def __str__(self):
        return 'crossing %d [%d,%d]' % (self.index, self.x, self.y)

        

class beamsplitter:
    def __init__(self, x, y, index, ratio=.5):
        ''' a splitter '''
        self.x=x
        self.y=y
        self.index=index
        self.set_splitting_ratio(ratio)
        
    def set_splitting_ratio(self, splitting_ratio):
        ''' change my degree of freedom '''
        self.splitting_ratio=splitting_ratio % 1
        
    def get_unitary(self):
        ''' get my unitary '''
	return np.matrix([[np.sqrt(self.splitting_ratio), 1j*np.sqrt(1-self.splitting_ratio)],[1j*np.sqrt(1-self.splitting_ratio), np.sqrt(self.splitting_ratio)]], dtype=complex)
        #return np.matrix([[1,1],[1,-1]])/np.sqrt(2)
        
    def draw(self, axis, text=True):
        ''' draw the splitter '''
        shape1x=np.array([0, 0.2, 0.8, 1])
        shape1y=np.array([0, 0, 1, 1])
        shape2x=np.array([0, 0.2, 0.8, 1])
        shape2y=np.array([1, 1, 0, 0])
        t=.2
        shape3x=np.array([0.5-t, 0.5+t])
        shape3y=np.array([.5,.5])
        axis.plot(shape1x+self.x, shape1y+self.y, 'k-')
        axis.plot(shape2x+self.x, shape2y+self.y, 'k-')
        axis.plot(shape3x+self.x, shape3y+self.y, 'k-', alpha=self.splitting_ratio)
        if text:
            color='#880000'
            axis.text(self.x+.5, self.y+.2, 'S%d' % self.index, color=color, fontsize=5, ha='center', va='bottom')
            axis.text(self.x+.8, self.y+.5, 'r=%.1f' % self.splitting_ratio, color=color, fontsize=5, ha='left', va='center')
        
    def __str__(self):
        ''' print '''
        return 'splitter %d [%d,%d]      \t| splitting_ratio =%.2f' % (self.index, self.x, self.y, self.splitting_ratio)

class phaseshifter:
    def __init__(self, x, y, index, phase=0, invert=False):
        ''' a splitter '''
        self.x=x
        self.y=y
        self.index=index
        self.invert=invert
        self.set_phi(phase)
        
    def set_phi(self, phi):
        ''' change my degree of freedom '''
        self.phi=phi % (2*np.pi)
        
    def get_unitary(self):
        ''' get my unitary '''
        if self.invert:
            return np.matrix([[np.exp(1j*self.phi),0],[0,1]], dtype=complex)
        else:
            return np.matrix([[1,0],[0,np.exp(1j*self.phi)]], dtype=complex)
        
    def draw(self, axis, text=True):
        ''' draw the splitter '''
        l=.1
        xo=np.sin(self.phi)*.1
        yo=np.cos(self.phi)*.1
        x,y = (self.x, self.y) if self.invert else (self.x, self.y+1)
        axis.plot([x+.5], [y], 'k.', zorder=150)
        p=axis.plot([x+.5, x+.5+xo], [y, y-yo], lw=1, color='red', zorder=100)
        
        if text:
            axis.text(self.x+.5, self.y+.8, 'P%d' % self.index, color='#4444ff', fontsize=5, ha='center', va='center')
        
    def __str__(self):
        ''' print '''
        return 'phase shifter %d [%d,%d] \t| phase =%.2f pi' % (self.index, self.x, self.y, self.phi/np.pi)


class beamsplitter_network:
    '''an object which describes a beamsplitter network'''
    def __init__(self, nmodes=None, json=None):
        self.nmodes = nmodes
        self.name='beamsplitter network'
        self.structure=[]
        self.phaseshifters=[]
        self.crossings=[]
        self.beamsplitters=[]
        self.input_modes=[]
        self.unitary=None
        if json!=None: self.from_json(json)

    def from_json(self, json_filename):
        ''' build the structure '''
        f=open(json_filename)
        jsondata=json.load(f, object_hook=json_no_unicode)
        f.close()
        self.nmodes=jsondata['modes']
        self.name=jsondata['name']
        self.width=jsondata['width']
        things=jsondata['couplers']+jsondata['shifters']
        things=sorted(things, key=lambda thing: thing['x'])
        for thing in things:
            if 'phase' in thing:
                self.add_phaseshifter(thing['x'], thing['y'])
            elif 'ratio' in thing:
                self.add_beamsplitter(thing['x'], thing['y'], thing['ratio'])
        self.get_unitary()

    def get_ndof(self):
        '''get the number of degrees of freedom'''
        return len(self.phaseshifters)+len(self.beamsplitters)

    def set_input_modes(self, mode_list):
        ''' set the input modes '''
        self.input_modes=mode_list

    def add_beamsplitter(self, x, y, splitting_ratio=.5):
        '''add a beamsplitter at position (x,y)'''
        bs=beamsplitter(x,y, len(self.beamsplitters), splitting_ratio)
        self.structure.append(bs)
        self.beamsplitters.append(bs)
        
    def add_crossing(self,x,y):
        cross=crossing(x,y,len(self.crossings))
        self.structure.append(cross)
        self.crossings.append(cross)

    def add_phaseshifter(self, x, y, phase=0, invert=False):
        '''add a beamsplitter at position (x,y)'''
        ps=phaseshifter(x,y, len(self.phaseshifters), phase, invert)
        self.structure.append(ps)
        self.phaseshifters.append(ps)
        
    def set_phases(self, new_phases):
        ''' set the phases '''
        for shifter, phase in zip(self.phaseshifters, new_phases):  
            shifter.set_phi(phase)
        self.get_unitary()
   
    def set_splitting_ratios(self, new_splitting_ratios):
        ''' set the phases '''
        for splitter, splitting_ratio in zip(self.beamsplitters, new_splitting_ratios): 
            splitter.set_splitting_ratio(splitting_ratio)
        self.get_unitary()

    def set_parameters(self, p):
        ''' set all parameters'''
        nps=len(self.phaseshifters)
        self.set_phases(p[:nps])
        self.set_splitting_ratios(p[nps:])
        self.get_unitary()

    def get_unitary(self):
        ''' build the unitary '''
        #TODO: this can be optimized by generating columns	
        self.unitary=np.matrix(np.eye(self.nmodes), dtype=complex)
        for o in reversed(self.structure):
            u=np.matrix(np.eye(self.nmodes, dtype=complex))
            u[o.y:o.y+2, o.y:o.y+2]=o.get_unitary()
            self.unitary*=u
        return self.unitary
    
    def __str__(self):
        ''' make a string representing the beamsplitter network '''
        s='%d-mode %s\n' % (self.nmodes, self.name)
        s+='%d phase shifters | ' % len(self.phaseshifters)
        s+='%d beam splitters | ' % len(self.beamsplitters)
        s+='%d degrees of freedom\n' % (len(self.phaseshifters)+len(self.beamsplitters))

        for i, component in enumerate(self.structure):
            s+='  (#%d) %s\n' % (i, str(component))
        return s

    def draw(self, filename='figures/out.pdf'):
        ''' draw the thing '''
        #print 'drawing beamsplitter network...',
        if len(self.structure)==0:
            max_x=1
        else:
            max_x=max([q.x for q in self.structure])

        # build a figure and some axes
        self.figure=Figure(figsize=(10*(max_x+2)/10.,5*self.nmodes/10.))
        self.canvas=FigureCanvas(self.figure)
        self.axes=self.figure.add_subplot(111)
        self.axes.axis('off')       

        # draw and label the modes
        for i in range(self.nmodes):
            self.axes.plot([-1, max_x+2], [i,i], '-', color='#cccccc')
            self.axes.text(-1.2, i, '%d' % i, va='center', fontsize=8, ha='center')
            self.axes.text(max_x+4-1.8, i, '%d' % i, va='center', fontsize=8, ha='center')
            #if i in self.inputs: self.axes.plot([-1.5], [i], 'ro')

        # draw the input photons
        for offset, group in enumerate(self.input_modes):
            x=-1.9+offset*.1
            self.axes.plot([x, x], [0, self.nmodes-1], '-', color='#ffcccc')
            old_g=None
            for g in group:
                if g==old_g: 
                    x+=.05
                else:
                    x=-1.9+offset*.1
                self.axes.plot(x, g, 'r.')
                old_g=g
        
        # draw all the beamsplitters and phase shifters
        for object in self.structure:
            object.draw(axis=self.axes, text=self.nmodes<20)
                
        self.axes.set_ylim((self.nmodes-.5),-1)
        self.axes.set_xlim(-2, max_x+3)
        self.axes.set_aspect(.5)
        self.canvas.print_figure(filename, bbox_inches='tight')
        #print 'done'


class reck_scheme(beamsplitter_network):
    ''' builds beamsplitter networks according to reck et al'''
    def __init__(self, nmodes, dense_phase_shifters=False):
        ''' dense phase shifters gives us more PS than we strictly need '''
        self.name='reck scheme'
        self.nmodes=nmodes
        self.dense_phase_shifters=dense_phase_shifters
        self.structure=[]
        self.phaseshifters=[]
        self.beamsplitters=[]
        self.input_modes=[]
        self.build()
        self.get_unitary()

    def build_column(self, x, height):
        ''' build a column '''
        splitter_y=lambda x: range(x%2,x+1,2)
        if self.dense_phase_shifters:
            phase_y=lambda x: range(x%2,x+1,2)
        else:
            phase_y=lambda x: range(0,x+1,2) if x%2==0 else []

        for y in phase_y(height):
            self.add_phaseshifter(x,self.nmodes-2-y, invert=True)
        for y in splitter_y(height):
            self.add_beamsplitter(x,self.nmodes-2-y)

    def build(self):
        ''' build the structure '''
        #if self.dense_phase_shifters: self.ps_column()
        # first triangle
        for x in range(self.nmodes-1):
            self.build_column(x, x)
        # second triangle
        for x in range(self.nmodes-1, self.nmodes*2-1):
            height=self.nmodes*2-4-x
            self.build_column(x, height)
