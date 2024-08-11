from manimlib.imports import*

class CreateBug(Scene):
    def construct(self):
        bug1 = ParametricFunction(
            lambda t: np.array([
                4*(np.cos(2*TAU*t))*(np.cos(1*TAU*t)),
                4*(np.cos(2*TAU*t))*(np.sin(1*TAU*t)),
                0
            ]),
           # t_min=2.64*PI/64, t_max=5.08*PI/64, step_size=0.04, color=BLUE
            t_min=2.55*PI/64, t_max=5.08*PI/64, step_size=0.04, color=BLUE
        )
        bug2 = ParametricFunction(
            lambda t: np.array([
                1.75*(np.cos(2*TAU*t))*(np.cos(1*TAU*t)),
                1.75*(np.cos(2*TAU*t))*(np.sin(1*TAU*t)),
                0
            ]),
            #t_min=0*PI/64, t_max=64*PI/64, step_size=0.04, color=BLUE
            t_min=7.95*PI/64, t_max=12.565*PI/64, step_size=0.04, color=BLUE
        )
        bug3 = ParametricFunction(
            lambda t: np.array([
                1.9*(np.cos(2*TAU*t))*(np.cos(1*TAU*t)),
                1.9*(np.cos(2*TAU*t))*(np.sin(1*TAU*t)),
                0
            ]),
            #t_min=0*PI/64, t_max=64*PI/64, step_size=0.04, color=BLUE
            t_min=7.75*PI/64, t_max=12.485*PI/64, step_size=0.04, color=BLUE
        )
        c1=Arc(radius=0.45,start_angle=PI/2,angle=PI,color=BLUE).shift(2.25*UP)
        c2=Arc(radius=0.1,start_angle=PI/3,angle=PI,color=BLUE).shift(0.6*LEFT+2.8*UP)
        l1=Polygon(np.array([0,-3,0]),np.array([0,3,0]),color=BLUE)
        l2=Polygon(np.array([0,0,0]),0.4*np.array([-0.5,0.87,0]),color=BLUE).shift(0.35*LEFT+2.55*UP)
        bug1.shift(2*UP)
        bug2.shift(0.85*LEFT+0.05*DOWN).rotate(-PI/8)#.set_fill(color=BLUE,opacity=0.5)
        bug3.shift(0.85*LEFT+1.05*DOWN).rotate(PI/6)#.set_fill(color=BLUE,opacity=0.5)
        bu1=VGroup(bug1,bug2,bug3,c1)
        bu2=VGroup(bu1,c2,l2)
        bu22=bu2.copy()
        bu3=bu2.copy().flip(UP).shift(2.62*RIGHT)
        bu33=bu3.copy()
        bug=VGroup(bu22,bu33)
        bu1.set_fill(color=BLUE,opacity=0.5)
        self.play(ShowCreation(bu2),ShowCreation(bug),ShowCreation(bu3),ShowCreation(l1),run_time=2)
        #self.play(ShowCreation(bug1),ShowCreation(c1),ShowCreation(c2),ShowCreation(l1),ShowCreation(l2),ShowCreation(bug2),ShowCreation(bug3),run_time=2)
        self.wait(2)

        self.play(FadeOut(bug),FadeOut(l1),ApplyMethod(bu2.shift,2*LEFT),ApplyMethod(bu3.shift,2*RIGHT))
        self.wait(1)
        self.play(ApplyMethod(bu2.flip,UP))
        self.play(ApplyMethod(bu2.shift,6.62*RIGHT))
        self.wait(1)
        self.play(ApplyMethod(bu2.flip,DOWN))
        self.play(ApplyMethod(bu2.shift,6.62*LEFT))
        self.wait(2)

        txt=TextMobject("\dn How many equal parts of bug are filled =").to_edge(UP)
        self.play(ShowCreation(txt))
        self.wait(1)
        txtt1=TextMobject("1",color=YELLOW_D).move_to(bu2.get_center()+1*RIGHT+0.5*DOWN)
        self.play(ShowCreation(txtt1))
        self.wait(1)
        self.play(ApplyMethod(txtt1.move_to,txt.get_center()+5*RIGHT))
        self.wait(1)

        txtt=TextMobject("The total number of equal parts of bug = ").to_edge(DOWN)
        self.play(ShowCreation(txtt))
        self.wait(1)
        txt1=TextMobject("1",color=RED_D).move_to(bu2.get_center()+1*RIGHT+0.5*DOWN)
        txtt2=TextMobject("2",color=RED_D).move_to(bu3.get_center()+1*LEFT+0.5*DOWN)
        self.play(ShowCreation(txt1))
        self.play(ShowCreation(txtt2))
        self.wait(1)
        self.play(FadeOut(txt1),ApplyMethod(txtt2.move_to,txtt.get_center()+5*RIGHT))
        self.wait(1)

        self.play(FadeIn(bug),FadeIn(l1),ApplyMethod(bu2.shift,2*RIGHT),ApplyMethod(bu3.shift,2*LEFT))
        self.wait(1)
        
        txt1=TextMobject("Fraction = --- ").next_to(bu3,2*RIGHT)
        self.play(ShowCreation(txt1))
        self.wait(1)
        self.play(FadeOut(txt),FadeOut(txtt),ApplyMethod(txtt1.move_to,txt1.get_center()+1.3*RIGHT+0.3*UP),ApplyMethod(txtt2.move_to,txt1.get_center()+1.3*RIGHT+0.45*DOWN))
        self.wait(2)
        