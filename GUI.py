import tkinter as tk
from InterpolationClass import InterpolationClass

from InterfaceToSQL import MyConnector as Connector

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.connector = Connector('127.0.0.1', '3306', 'interpolations_output', 'root', 'F0ll0wSQL')
        self.picture = InterpolationClass()
        self.output = None
        self.keys = None
        self.time = 0
        self.polygon_coords = {}
        self.polygon_coords['xy'] = []
        self.polygon_coords['xz'] = []
        self.polygon_coords['zy'] = []
        self.label_vx0 = tk.Label(self, text='Vx0')
        self.label_vy0 = tk.Label(self, text='Vy0')
        self.label_vz0 = tk.Label(self, text='Vz0')
        self.label_x0 = tk.Label(self, text='X0')
        self.label_y0 = tk.Label(self, text='Y0')
        self.label_z0 = tk.Label(self, text='Z0')
        self.label_t0 = tk.Label(self, text='t0')
        self.label_t = tk.Label(self, text='t')
        self.label_H1 = tk.Label(self, text='Секунды')
        self.label_H2 = tk.Label(self, text='Секунды') 
        self.label_ax = tk.Label(self, text='Ax')
        self.label_ay = tk.Label(self, text='Ay')
        self.label_az = tk.Label(self, text='Az')
        self.label_vx = tk.Label(self, text='Vx')
        self.label_vy = tk.Label(self, text='Vy')
        self.label_vz = tk.Label(self, text='Vz')
        self.label_x = tk.Label(self, text='X')
        self.label_y = tk.Label(self, text='Y')
        self.label_z = tk.Label(self, text='Z')
        self.label_min = tk.Label(self, text='Min')
        self.label_max = tk.Label(self, text='Max')
        self.label_step_h = tk.Label(self, text='Шаг h')

        self.entry_vx0 = tk.Entry(self)
        self.entry_vy0 = tk.Entry(self)
        self.entry_vz0 = tk.Entry(self)
        self.entry_ax0 = tk.Entry(self)
        self.entry_ay0 = tk.Entry(self)
        self.entry_az0 = tk.Entry(self)
        self.entry_x0 = tk.Entry(self)
        self.entry_y0 = tk.Entry(self)
        self.entry_z0 = tk.Entry(self)
        self.entry_t0 = tk.Entry(self)
        self.entry_vx = tk.Entry(self)
        self.entry_vy = tk.Entry(self)
        self.entry_vz = tk.Entry(self)
        self.entry_ax = tk.Entry(self)
        self.entry_ay = tk.Entry(self)
        self.entry_az = tk.Entry(self)
        self.entry_x = tk.Entry(self)
        self.entry_y = tk.Entry(self)
        self.entry_z = tk.Entry(self)
        self.entry_t = tk.Entry(self)

        self.entry_vx0.insert(0, '0')
        self.entry_vy0.insert(0, '0.026')
        self.entry_vz0.insert(0, '0.01')
        self.entry_x0.insert(0, '0.5')
        self.entry_y0.insert(0, '0.5')
        self.entry_z0.insert(0, '0.2')
        self.entry_t0.insert(0, '0')
        self.entry_t.insert(0, '4000')
        self.entry_vx['state'] = tk.DISABLED
        self.entry_vy['state'] = tk.DISABLED
        self.entry_vz['state'] = tk.DISABLED
        self.entry_ax['state'] = tk.DISABLED
        self.entry_ay['state'] = tk.DISABLED
        self.entry_az['state'] = tk.DISABLED
        self.entry_x['state'] = tk.DISABLED
        self.entry_y['state'] = tk.DISABLED
        self.entry_z['state'] = tk.DISABLED
        
        self.computate = tk.Button(self, text='Рассчитать', command=self.computation)

        self.scale = tk.Scale(self, orient=tk.HORIZONTAL, length=400, from_=1, to=1, tickinterval=1,
               resolution=1, command=self.output_data)

        self.canvas_xy = tk.Canvas(self, width=0, height=0)
        self.canvas_zy = tk.Canvas(self, width=0, height=0)
        self.canvas_xz = tk.Canvas(self, width=0, height=0)
        
        self.label_vx0.grid(row=1, column=1)
        self.label_vy0.grid(row=1, column=2)
        self.label_vz0.grid(row=1, column=3)
        self.entry_vx0.grid(row=2, column=1)
        self.entry_vy0.grid(row=2, column=2)
        self.entry_vz0.grid(row=2, column=3)
        self.label_x0.grid(row=3, column=1)
        self.label_y0.grid(row=3, column=2)
        self.label_z0.grid(row=3, column=3)
        self.entry_x0.grid(row=4, column=1)
        self.entry_y0.grid(row=4, column=2)
        self.entry_z0.grid(row=4, column=3)
        self.label_t0.grid(row=5, column=1, columnspan=3)
        self.entry_t0.grid(row=6, column=1, columnspan=2)
        self.label_t.grid(row=7, column=1, columnspan=3)
        self.entry_t.grid(row=8, column=1, columnspan=2)
        self.label_H1.grid(row=6, column=3)
        self.label_H2.grid(row=8, column=3)
        self.computate.grid(row=9, column=1, columnspan=3)
        self.label_ax.grid(row=10, column=1)
        self.label_ay.grid(row=10, column=2)
        self.label_az.grid(row=10, column=3)
        self.entry_ax.grid(row=11, column=1)
        self.entry_ay.grid(row=11, column=2)
        self.entry_az.grid(row=11, column=3)
        self.label_vx.grid(row=12, column=1)
        self.label_vy.grid(row=12, column=2)
        self.label_vz.grid(row=12, column=3)
        self.entry_vx.grid(row=13, column=1)
        self.entry_vy.grid(row=13, column=2)
        self.entry_vz.grid(row=13, column=3)
        self.label_x.grid(row=14, column=1)
        self.label_y.grid(row=14, column=2)
        self.label_z.grid(row=14, column=3)
        self.entry_x.grid(row=15, column=1)
        self.entry_y.grid(row=15, column=2)
        self.entry_z.grid(row=15, column=3)
        self.label_step_h.grid(row=16, column=1, columnspan=3)
        self.scale.grid(row=17, column=1, columnspan=3)
        self.canvas_xy.grid(row=18, column=4)
        self.canvas_zy.grid(row=18, column=1, columnspan=3)
        self.canvas_xz.grid(row=1, column=4, rowspan=17)

    def computation(self):
        '''
            Эта функция запускается после нажатия кнопки
        '''
        self.picture.Input(
            float(self.entry_vx0.get()), 
            float(self.entry_vy0.get()),
            float(self.entry_vz0.get()),
            float(self.entry_x0.get()),
            float(self.entry_y0.get()),
            float(self.entry_z0.get()),
            float(self.entry_t0.get()),
            float(self.entry_t.get())
            )
        self.output, self.keys = self.picture.Calc()
        """
        for i in range(0, len(self.keys), 60):
            self.connector.insert(table='variables', 
                                Vx=str(self.output[self.keys[i]]['vx']),
                                Vy=str(self.output[self.keys[i]]['vy']),
                                Vz=str(self.output[self.keys[i]]['vz']),
                                Ax=str(self.output[self.keys[i]]['ax']),
                                Ay=str(self.output[self.keys[i]]['ay']),
                                Az=str(self.output[self.keys[i]]['az']),
                                X=str(self.output[self.keys[i]]['x']),
                                Y=str(self.output[self.keys[i]]['y']),
                                Z=str(self.output[self.keys[i]]['z']),
                                Time=self.keys[i])
"""
        self.entry_vx['state'] = tk.NORMAL
        self.entry_vy['state'] = tk.NORMAL
        self.entry_vz['state'] = tk.NORMAL
        self.entry_ax['state'] = tk.NORMAL
        self.entry_ay['state'] = tk.NORMAL
        self.entry_az['state'] = tk.NORMAL
        self.entry_x['state'] = tk.NORMAL
        self.entry_y['state'] = tk.NORMAL
        self.entry_z['state'] = tk.NORMAL
        
        self.entry_vx.delete(0, 'end')
        self.entry_vy.delete(0, 'end')
        self.entry_vz.delete(0, 'end')
        self.entry_ax.delete(0, 'end')
        self.entry_ay.delete(0, 'end')
        self.entry_az.delete(0, 'end')
        self.entry_x.delete(0, 'end')
        self.entry_y.delete(0, 'end')
        self.entry_z.delete(0, 'end')
        
        self.entry_vx.insert(0, str(self.output[self.keys[0]]['vx']))
        self.entry_vy.insert(0, str(self.output[self.keys[0]]['vy']))
        self.entry_vz.insert(0, str(self.output[self.keys[0]]['vz']))
        self.entry_ax.insert(0, str(self.output[self.keys[0]]['ax']))
        self.entry_ay.insert(0, str(self.output[self.keys[0]]['ay']))
        self.entry_az.insert(0, str(self.output[self.keys[0]]['az']))
        self.entry_x.insert(0, str(self.output[self.keys[0]]['x']))
        self.entry_y.insert(0, str(self.output[self.keys[0]]['y']))
        self.entry_z.insert(0, str(self.output[self.keys[0]]['z']))

        self.entry_vx['state'] = tk.DISABLED
        self.entry_vy['state'] = tk.DISABLED
        self.entry_vz['state'] = tk.DISABLED
        self.entry_ax['state'] = tk.DISABLED
        self.entry_ay['state'] = tk.DISABLED
        self.entry_az['state'] = tk.DISABLED
        self.entry_x['state'] = tk.DISABLED
        self.entry_y['state'] = tk.DISABLED
        self.entry_z['state'] = tk.DISABLED

        self.scale['from_'] = self.keys[0]
        self.scale['to'] = self.keys[len(self.keys)-1] - 60
        self.scale['tickinterval'] = self.keys[len(self.keys)-1] - self.keys[0]
        self.scale['resolution'] = 60
        
        self.init_reposition_variables()
        self.draw()
        self.update()

    def output_data(self, time):
        self.time = int(time)
        self.entry_vx['state'] = tk.NORMAL
        self.entry_vy['state'] = tk.NORMAL
        self.entry_vz['state'] = tk.NORMAL
        self.entry_ax['state'] = tk.NORMAL
        self.entry_ay['state'] = tk.NORMAL
        self.entry_az['state'] = tk.NORMAL
        self.entry_x['state'] = tk.NORMAL
        self.entry_y['state'] = tk.NORMAL
        self.entry_z['state'] = tk.NORMAL
        
        self.entry_vx.delete(0, 'end')
        self.entry_vy.delete(0, 'end')
        self.entry_vz.delete(0, 'end')
        self.entry_ax.delete(0, 'end')
        self.entry_ay.delete(0, 'end')
        self.entry_az.delete(0, 'end')
        self.entry_x.delete(0, 'end')
        self.entry_y.delete(0, 'end')
        self.entry_z.delete(0, 'end')
        
        self.entry_vx.insert(0, str(self.output[self.keys[self.time]]['vx']))
        self.entry_vy.insert(0, str(self.output[self.keys[self.time]]['vy']))
        self.entry_vz.insert(0, str(self.output[self.keys[self.time]]['vz']))
        self.entry_ax.insert(0, str(self.output[self.keys[self.time]]['ax']))
        self.entry_ay.insert(0, str(self.output[self.keys[self.time]]['ay']))
        self.entry_az.insert(0, str(self.output[self.keys[self.time]]['az']))
        self.entry_x.insert(0, str(self.output[self.keys[self.time]]['x']))
        self.entry_y.insert(0, str(self.output[self.keys[self.time]]['y']))
        self.entry_z.insert(0, str(self.output[self.keys[self.time]]['z']))

        self.entry_vx['state'] = tk.DISABLED
        self.entry_vy['state'] = tk.DISABLED
        self.entry_vz['state'] = tk.DISABLED
        self.entry_ax['state'] = tk.DISABLED
        self.entry_ay['state'] = tk.DISABLED
        self.entry_az['state'] = tk.DISABLED
        self.entry_x['state'] = tk.DISABLED
        self.entry_y['state'] = tk.DISABLED
        self.entry_z['state'] = tk.DISABLED

        self.draw()

    def init_reposition_variables(self):
        self.maximum_x = self.output[self.keys[0]]['x']
        self.maximum_y = self.output[self.keys[0]]['y']
        self.maximum_z = self.output[self.keys[0]]['z']
        self.minimum_x = self.output[self.keys[0]]['x']
        self.minimum_y = self.output[self.keys[0]]['y']
        self.minimum_z = self.output[self.keys[0]]['z']
        for i in self.output:
            if self.output[i]['x'] > self.maximum_x:
                self.maximum_x = self.output[i]['x']
            if self.output[i]['x'] < self.minimum_x:
                self.minimum_x = self.output[i]['x']
            if self.output[i]['y'] > self.maximum_y:
                self.maximum_y = self.output[i]['y']
            if self.output[i]['y'] < self.minimum_y:
                self.minimum_y = self.output[i]['y']
            if self.output[i]['z'] > self.maximum_z:
                self.maximum_z = self.output[i]['z']
            if self.output[i]['z'] < self.minimum_z:
                self.minimum_z = self.output[i]['z']

        self.polygon_coords['xy'].clear()
        self.polygon_coords['xz'].clear()
        self.polygon_coords['zy'].clear()        
        for i in self.keys:
            x, y, z = self.output[i]['x'], self.output[i]['y'], self.output[i]['z']
            self.polygon_coords['xy'].append((x - self.minimum_x) * (390 - 10) / (self.maximum_x - self.minimum_x) + 10)
            self.polygon_coords['xy'].append((y - self.minimum_y) * (390 - 10) / (self.maximum_y - self.minimum_y) + 10)
            self.polygon_coords['xz'].append((x - self.minimum_x) * (390 - 10) / (self.maximum_x - self.minimum_x) + 10)
            self.polygon_coords['xz'].append((z - self.minimum_z) * (390 - 10) / (self.maximum_z - self.minimum_z) + 10)
            self.polygon_coords['zy'].append((z - self.minimum_z) * (390 - 10) / (self.maximum_z - self.minimum_z) + 10)
            self.polygon_coords['zy'].append((y - self.minimum_y) * (390 - 10) / (self.maximum_y - self.minimum_y) + 10)

    def draw(self):
        self.canvas_xy.delete('ALL')
        self.canvas_zy.delete('ALL')
        self.canvas_xz.delete('ALL')
        self.canvas_xy.create_rectangle(-1, -1, 2000, 2000, fill='white')
        self.canvas_zy.create_rectangle(-1, -1, 2000, 2000, fill='white')
        self.canvas_xz.create_rectangle(-1, -1, 2000, 2000, fill='white')
        
        self.canvas_xz['height'] = self.canvas_zy['width'] = 400
        self.canvas_xy['width'] = self.canvas_xz['width'] = 400
        self.canvas_xy['height'] = self.canvas_zy['height'] = 400
        
        x, y, z = self.output[self.keys[self.time]]['x'], self.output[self.keys[self.time]]['y'], self.output[self.keys[self.time]]['z']

        x = (x - self.minimum_x) * (390 - 10) / (self.maximum_x - self.minimum_x) + 10 
        y = (y - self.minimum_y) * (390 - 10) / (self.maximum_y - self.minimum_y) + 10 
        z = (z - self.minimum_z) * (390 - 10) / (self.maximum_z - self.minimum_z) + 10

        self.canvas_xy.create_line(*self.polygon_coords['xy'], fill=None)
        self.canvas_zy.create_line(*self.polygon_coords['zy'], fill=None)
        self.canvas_xz.create_line(*self.polygon_coords['xz'], fill=None)

        self.canvas_xy.create_oval(x-5, y-5, x+5, y+5)
        self.canvas_zy.create_oval(z-5, y-5, z+5, y+5)
        self.canvas_xz.create_oval(x-5, z-5, x+5, z+5)

        self.canvas_xy.update()
        self.canvas_zy.update()
        self.canvas_xz.update()