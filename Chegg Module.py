#!/usr/bin/env python
# coding: utf-8


class SS:
    def __init__(self):
        import statistics
        self.__st=statistics
        
    def ss1_str(self,v):
        ss1_str=[]
        #ss_cal=[]
        me=round(self.__st.mean(v),4)
        for i in v:
            dev=(i-me)
            dev1=round(dev,4)
            ss_1=f'({i}-{me})^2' if me>=0 else f'({i}-({me}))^2'
            ss1_str.append(ss_1)
        return ss1_str
            
    def ss2_str(self,v):
        ss2_str=[]
        me=round(self.__st.mean(v),4)
        for i in v:
            dev=(i-me)
            dev1=round(dev,4)
            ss_2=f'{dev1}^2' if dev>=0 else f"({dev1})^2"
            ss2_str.append(ss_2)
        return ss2_str
            
    def ss3_list(self,v):
        ss3_list=[]
        me=round(self.__st.mean(v),4)
        for i in v:
            dev=(i-me)
            dev1=round(dev,4)
            ss_3=round(dev1**2,4)
            ss3_list.append(ss_3)
        return ss3_list
    
    def ss_cal(self,v):
        ss_cal=[]
        me=round(self.__st.mean(v),4)
        for i in v:
            dev=(i-me)
            dev1=round(dev,4)
            ss_cal.append(dev**2)
        return ss_cal
    
    

class Chegg:
    def __init__(self,x=None,y=None):
        self.__x=x
        self.__y=y
        self.SS=SS()
        
        import statistics
        import math as m
        import scipy.stats as stats
        from IPython.display import display
        from IPython.display import Math
        from IPython.display import Markdown
        import numpy
        from sklearn.linear_model import LinearRegression
        
        self.__st=statistics
        self.__m=m
        self.__stats=stats
        self.__display=display
        self.__Math=Math
        self.__Markdown=Markdown
        self.__np=numpy
        self.__LR=LinearRegression
        
    @staticmethod
    def __short(l):
        try:
            s_l=[]
            s_l1=[]
            for i in l:
                s_l.append(f"{i}")
            for j in s_l:
                j=f"({j})" if j[0]=="-" else f"{j}"
                s_l1.append(j)
            sh=f"{'+'.join(s_l1[0:2])}+...+{s_l1[-1]}" if len(l)>3 else f"{'+'.join(s_l1)}"
            return sh

        except TypeError:
            # Code that handles the exception
            print("Error: You entered wrong data type, Please provide a List")
            
            
    def Mean_c(self, var, var_name=None):
        if var_name is None:
            var_name = input("Enter variable name: ")

        try:
            var_str_L = [f'({i})' if i < 0 else str(i) for i in var]

            self.__display(self.__Markdown("# Mean"))
            self.__display(self.__Math(fr"\bar{{{var_name}}}=\sum_{{i=1}}^{{n}} \frac{{{var_name}_i}}{{n}}"))
            print(f"bar{var_name}=(sum{var_name}_i)/n")
            print('------------------------------------------------------------------------')
            print(f'\nSTEP 01 :\nbar{var_name}=[{self.__short(var_str_L)}]/{len(var)}\n\nSTEP 02 :\n{sum(var)}/{len(var)}\n\nSTEP 03 :\n{sum(var)/len(var)}\n\nMean of "{var_name}" is :\n{round(sum(var)/len(var), 4)}')
            print('\n------------------------------------------------------------------------')

            # CROSS CHECK
            self.__display(self.__Markdown("## Cross check :"))

            print(f"Mean of {var_name}:\t", self.__st.mean(var))
            print("\n................................")

        except TypeError:
            print("Error: You entered the wrong data type. Please provide a list.")
            
            
    #Variance        
    def Variance_P_c(self,variable,var_name=None):
        if var_name is None:
            var_name = input("Enter variable name: ")

            
            self.__display(self.__Markdown("# Population Varience"))
            self.__display(self.__Math(fr"\sigma^2_{{{var_name}}}=\frac{{\sum_{{i=1}}^{{n}} ({var_name}_i - \bar{{{var_name}}})^2}}{{n}}"))
            print('------------------------------------------------------------------------')
            print(f'\nSTEP 00 :\nsigma^2_{var_name}=(sum({var_name}_i-bar{var_name})^2)/n')
            print(f'\nSTEP 01 :\n[{self.__short(self.SS.ss1_str(variable))}]/{len(variable)}')
            print(f'\nSTEP 02 :\n[{self.__short(self.SS.ss2_str(variable))}]/{len(variable)}')
            print(f'\nSTEP 03 :\n[{self.__short(self.SS.ss3_list(variable))}]/{len(variable)}')
            print(f'\nSTEP 04 :\n{sum(self.SS.ss_cal(variable))/len(variable)}')
            print(f'\nPopulation Variance of "{var_name}" is :\n{round(sum(self.SS.ss_cal(variable))/len(variable), 4)}\n<<...Rounded to four decimal...>>')
            print('\n------------------------------------------------------------------------')

            # CROSS CHECK
            self.__display(self.__Markdown("## Cross check :"))

            print(f"Population Variance of {var_name}:\t", self.__st.pvariance(variable))
            print("\n................................")
            
            
            
    def Variance_S_c(self,variable,var_name=None):
        if var_name is None:
            var_name = input("Enter variable name: ")

            
            self.__display(self.__Markdown("# Sample Varience"))
            self.__display(self.__Math(fr"\\S^2_{{{var_name}}}=\frac{{\sum_{{i=1}}^{{n-1}} ({var_name}_i - \bar{{{var_name}}})^2}}{{n-1}}"))
            print('------------------------------------------------------------------------')
            print(f'\nSTEP 00 :\nS^2_{var_name}=(sum({var_name}_i-bar{var_name})^2)/(n-1)')
            print(f'\nSTEP 01 :\n[{self.__short(self.SS.ss1_str(variable))}]/({len(variable)}-1)')
            print(f'\nSTEP 02 :\n[{self.__short(self.SS.ss2_str(variable))}]/{len(variable)-1}')
            print(f'\nSTEP 03 :\n[{self.__short(self.SS.ss3_list(variable))}]/{len(variable)-1}')
            print(f'\nSTEP 04 :\n{sum(self.SS.ss_cal(variable))/(len(variable)-1)}')
            print(f'\nSample Variance of "{var_name}" is :\n{round(sum(self.SS.ss_cal(variable))/(len(variable)-1), 4)}\n<<...Rounded to four decimal...>>')
            print('\n------------------------------------------------------------------------')

            # CROSS CHECK
            self.__display(self.__Markdown("## Cross check :"))

            print(f"Sample Variance of {var_name}:\t", self.__st.variance(variable))
            print("\n................................")
        
 

    #Standard Deviation
    def StandardDev_P_c(self,variable,var_name=None):
        if var_name is None:
            var_name = input("Enter variable name: ")

            
            self.__display(self.__Markdown("# Population SD"))
            self.__display(self.__Math(fr"\sigma_{{{var_name}}}=\sqrt\frac{{\sum_{{i=1}}^{{n}} ({var_name}_i - \bar{{{var_name}}})^2}}{{n}}"))
            print('------------------------------------------------------------------------')
            print(f'\nSTEP 00 :\nsigma_{var_name}=sqrt((sum({var_name}_i-bar{var_name})^2)/n)')
            print(f'\nSTEP 01 :\nsqrt([{self.__short(self.SS.ss1_str(variable))}]/{len(variable)})')
            print(f'\nSTEP 02 :\nsqrt([{self.__short(self.SS.ss2_str(variable))}]/{len(variable)})')
            print(f'\nSTEP 03 :\nsqrt([{self.__short(self.SS.ss3_list(variable))}]/{len(variable)})')
            print(f'\nSTEP 04 :\n{(sum(self.SS.ss_cal(variable))/len(variable))**0.5}')
            print(f'\nPopulation SD of "{var_name}" is :\n{round((sum(self.SS.ss_cal(variable))/len(variable))**0.5, 4)}\n<<...Rounded to four decimal...>>')
            print('\n------------------------------------------------------------------------')

            # CROSS CHECK
            self.__display(self.__Markdown("## Cross check :"))

            print(f"Population SD of {var_name}:\t", self.__st.pstdev(variable))
            print("\n................................")
            
    
    
    def StandardDev_S_c(self,variable,var_name=None):
        if var_name is None:
            var_name = input("Enter variable name: ")

            
        self.__display(self.__Markdown("# Sample SD"))
        self.__display(self.__Math(fr"\\S_{{{var_name}}}=\sqrt\frac{{\sum_{{i=1}}^{{n-1}} ({var_name}_i - \bar{{{var_name}}})^2}}{{n-1}}"))
        print('------------------------------------------------------------------------')
        print(f'\nSTEP 00 :\nS_{var_name}=sqrt((sum({var_name}_i-bar{var_name})^2)/(n-1))')
        print(f'\nSTEP 01 :\nsqrt([{self.__short(self.SS.ss1_str(variable))}]/({len(variable)}-1))')
        print(f'\nSTEP 02 :\nsqrt([{self.__short(self.SS.ss2_str(variable))}]/{len(variable)-1})')
        print(f'\nSTEP 03 :\nsqrt([{self.__short(self.SS.ss3_list(variable))}]/{len(variable)-1})')
        print(f'\nSTEP 04 :\n{(sum(self.SS.ss_cal(variable))/(len(variable)-1))**0.5}')
        print(f'\nPopulation SD of "{var_name}" is :\n{round((sum(self.SS.ss_cal(variable))/(len(variable)-1))**0.5, 4)}\n<<...Rounded to four decimal...>>')
        print('\n------------------------------------------------------------------------')

        # CROSS CHECK
        self.__display(self.__Markdown("## Cross check :"))

        print(f"Sample SD of {var_name}:\t", self.__st.stdev(variable))
        print("\n................................")
            
        
    def Correlation_c(self):
        nm=input("""Variables name, other than \"x\" and \"y\" ??
                 Enter y or n : """)
        if nm=="y" or nm=="Y":
            var1=input("Enter your first variable name : ")
            var2=input("Enter your second variable name : ")
        else:
            var1="x"
            var2="y"
            
        # mean
        mx=round(self.__st.mean(self.__x),4)
        my=round(self.__st.mean(self.__y),4)

        # containers
        str_xy_list=[]
        str1_xy_list=[]
        str2_xy_list=[]
        cal_xy_list=[]
    

        # code
        for i,j in zip(self.__x,self.__y):
            smx=f"({mx})" if mx<0 else mx    # conditional based string mean + and - 
            smy=f"({my})" if my<0 else my

            sxy=f'({i}-{smx}*{j}-{smy})' # brick string 1
            s1xy=f'({(i-mx):.4f}*{(j-my):.4f})' # brick string 1
            s2xy=f'({((i-mx)*(j-my)):.4f})' # brick sring 2
            calxy=((i-mx)*(j-my))        # brick calculation (new)

            # Append
            str_xy_list.append(sxy)
            str1_xy_list.append(s1xy)
            str2_xy_list.append(s2xy)
            cal_xy_list.append(calxy)

        self.__display(self.__Markdown("# Correlation"))
        print("\n................................")
        
        #Correlation
        devXY=self.__short(str_xy_list)
        devXY1=self.__short(str1_xy_list)
        devXY2=self.__short(str2_xy_list)


        
        self.__display(self.__Markdown("## Correlation coefficient :\n"))
        self.__display(self.__Math(fr"$Correlation(r) = \frac{{\sum_{{i=1}}^{{n}}({var1}_i - \bar{{{var1}}})({var2}_i - \bar{{{var2}}})}}{{\sqrt{{\sum_{{i=1}}^{{n}}({var1}_i - \bar{{{var1}}})^2 \sum_{{i=1}}^{{n}}({var2}_i - \bar{{{var2}}})^2}}}}$"))

        print(f"\nFormula :\nr=(sum({var1}-bar{var1})({var2}-bar{var2}))/sqrt(sum({var1}-bar{var1})^2*sum({var2}-bar{var2})^2)\n\n................................")
        self.__display(self.__Markdown("### Syntax 01 :"))
        self.__display(self.__Markdown("#### (Direct calculation) :"))
        
        print(f"\nSTEP 00 :\nr=(sum({var1}-bar{var1})({var2}-bar{var2}))/sqrt(sum({var1}-bar{var1})^2*sum({var2}-bar{var2})^2)")
        print(f"\nSTEP 01 :\n({devXY})/sqrt([{self.__short(self.SS.ss1_str(self.__x))}]*[{self.__short(self.SS.ss1_str(self.__y))}])")
        print(f"\nSTEP 02 :\n({devXY1})/sqrt([{self.__short(self.SS.ss2_str(self.__x))}]*[{self.__short(self.SS.ss2_str(self.__y))}])")
        print(f"\nSTEP 03 :\n({devXY2})/sqrt([{self.__short(self.SS.ss3_list(self.__x))}]*[{self.__short(self.SS.ss3_list(self.__y))}])")
        print(f"\nSTEP 04 :\n({round(sum(cal_xy_list),4)})/sqrt({round(sum(self.SS.ss_cal(self.__x))*sum(self.SS.ss_cal(self.__y)),4)})")
        print(f"\nSTEP 05 :\n({round(sum(cal_xy_list),4)})/({round((sum(self.SS.ss_cal(self.__x))*sum(self.SS.ss_cal(self.__y)))**0.5,4)})")
        print(f"\nSTEP 06 :\n{sum(cal_xy_list)/((sum(self.SS.ss_cal(self.__x))*sum(self.SS.ss_cal(self.__y)))**0.5)}")
        print("\n................................\n\n")
                
        
        # CROSS CHECK
        self.__display(self.__Markdown("## Cross check :"))
        print("Correlation is :\n",self.__np.corrcoef(self.__x,self.__y)[0,1])
        print("\n................................")
        
        
    def Cov_c(self):
        nm=input("""Variables name, other than \"x\" and \"y\" ??
                 Enter y or n : """)
        if nm=="y" or nm=="Y":
            var1=input("Enter your first variable name : ")
            var2=input("Enter your second variable name : ")
        else:
            var1="x"
            var2="y"
            
        # mean
        mx=round(self.__st.mean(self.__x),4)
        my=round(self.__st.mean(self.__y),4)

        # containers
        str_xy_list=[]
        str1_xy_list=[]
        str2_xy_list=[]
        cal_xy_list=[]
    

        # code
        for i,j in zip(self.__x,self.__y):
            smx=f"({mx})" if mx<0 else mx    # conditional based string mean + and - 
            smy=f"({my})" if my<0 else my

            sxy=f'({i}-{smx}*{j}-{smy})' # brick string 1
            s1xy=f'({(i-mx):.4f}*{(j-my):.4f})' # brick string 1
            s2xy=f'({((i-mx)*(j-my)):.4f})' # brick sring 2
            calxy=((i-mx)*(j-my))        # brick calculation (new)

            # Append
            str_xy_list.append(sxy)
            str1_xy_list.append(s1xy)
            str2_xy_list.append(s2xy)
            cal_xy_list.append(calxy)

        self.__display(self.__Markdown("# Covariance"))
        print("\n................................")
        
        
        devXY=self.__short(str_xy_list)
        devXY1=self.__short(str1_xy_list)
        devXY2=self.__short(str2_xy_list)


        
        self.__display(self.__Markdown("## Sample Covariance :\n"))
        self.__display(self.__Math(fr"\\S_{{xy}} = \frac{{\sum_{{i=1}}^{{n}}({var1}_i - \bar{{{var1}}})({var2}_i - \bar{{{var2}}})}}{{n-1}}"))

        print(f"\nFormula :\nS_(xy)=(sum({var1}-bar{var1})({var2}-bar{var2}))/(n-1)\n\n................................")
        self.__display(self.__Markdown("### Syntax 01 :"))
        self.__display(self.__Markdown("#### (Direct calculation) :"))
        
        print(f"\nSTEP 00 :\nS_(xy)=(sum({var1}-bar{var1})({var2}-bar{var2}))/(n-1)")
        print(f"\nSTEP 01 :\n({devXY})/({len(self.__x)}-1)")
        print(f"\nSTEP 02 :\n({devXY1})/{(len(self.__x)-1)}")
        print(f"\nSTEP 03 :\n({devXY2})/{(len(self.__x)-1)}")
        print(f"\nSTEP 04 :\n({round(sum(cal_xy_list),4)})/{(len(self.__x)-1)}")
        print(f"\nSTEP 05 :\n{sum(cal_xy_list)/(len(self.__x)-1)}")
        print("\n................................\n\n")
                
        
        # CROSS CHECK
        self.__display(self.__Markdown("## Cross check :"))
        print("Sample Covariance is :\n",self.__np.cov(self.__x,self.__y)[0,1])
        print("\n................................")
        
        
    def onesample_ttest_c(self,var=None,dt=None):
        var_name=input("Enter your variable name : ")
            
        if dt==None:
            dt=input("""
            Enter "0" for raw data
            Enter "1" for summerized data
            """)
        
        h1=input("""
        Type of Hypothesis
        Enter "1" for !=
        Enter "2" for <
        Enter "3" for >
        """)
    
        self.__display(self.__Markdown("## One Sample-t-test :\n"))
        self.__display(self.__Math(fr"\\t_{{cal}} = \frac{{(\bar{{{var_name}}}-\mu)}}{{s/\sqrt{{n}}}}"))

        print(f"\nFormula :\nt_(cal)=({var_name}-mu)/(s//sqrtn)\n\n................................")
            
        if dt=="0":
            self.__display(self.__Markdown("### Syntax 01 :"))
            self.__display(self.__Markdown("#### (Direct calculation) :"))


            print(f"Now,\nFirst we need to calculate Mean and standard deviation of {var_name}")
            print(f"\nMean of {var_name} is,")
            self.Mean_c(var,var_name)
            print(f"\nStanard deviation of {var_name} is,")
            self.StandardDev_S_c(var,var_name)
            
            mu=float(input(f"Hypothetical Mean (mu) :"))
            n=len(var)

            me=round(self.__st.mean(var),4)
            s=round(self.__st.stdev(var),4)

            #print("\n\n")
            self.__display(self.__Markdown("## Test Statistic:\n"))
            print("\n\nNow,\nTest Statistic is,")
            print(f"\nSTEP 00 :\nt_(cal)=(bar{var_name}-mu)/(s//sqrtn)")
            print(f"\nSTEP 01 :\n({me}-{mu})/({s}//sqrt{n})")
            print(f"\nSTEP 02 :\n({round((self.__st.mean(var)-mu),4)})/({round(self.__st.stdev(var)/(n**0.5),6)})")
            print(f"\nSTEP 03 :\n{(self.__st.mean(var)-mu)/(self.__st.stdev(var)/(n**0.5))}")
            print(f"\nSTEP 04 :\n{round(((self.__st.mean(var)-mu)/(self.__st.stdev(var)/(n**0.5))),4)}")
            print("\n................................\n\n")
            test_stat=round(((self.__st.mean(var)-mu)/(self.__st.stdev(var)/(n**0.5))),4)


            # CROSS CHECK
            self.__display(self.__Markdown("## Cross check :"))
            print("Test Statistic is :\n",self.__stats.ttest_1samp(var, mu))
            print("\n................................")
        
            ## critical value or p-value
            c=input("""
            Enter "0" for p-value
            Enter "1" for Critical value
            """)

            if c=="0":
                self.pvalue_c(h1,len(var)-1,test_stat)
            else:
                self.critical_t(h1,len(var)-1)     

        elif dt=="1":
            me=float(input(f"{var_name} bar :"))
            mu=float(input("Hypothetical Mean :"))
            s=float(input("Standard Deviation :"))
            n=int(input("Sample size :"))
                
            self.__display(self.__Markdown("### Syntax 02 :"))
            self.__display(self.__Markdown("#### (Summarized Data) :"))


            print("\n\n")
            self.__display(self.__Markdown("## Test Statistic:\n"))
            print("\n\nNow,\nTest Statistic is,")
            print(f"\nSTEP 00 :\nt_(cal)=(bar{var_name}-mu)/(s//sqrtn)")
            print(f"\nSTEP 01 :\n({me}-{mu})/({s}//sqrt{n})")
            print(f"\nSTEP 02 :\n({round((me-mu),4)})/({round(s/(n**0.5),6)})")
            print(f"\nSTEP 03 :\n{(me-mu)/(s/(n**0.5))}")
            print(f"\nSTEP 04 :\n{round(((me-mu)/(s/(n**0.5))),4)}")
            print("\n................................\n\n")
            test_stat=round(((me-mu)/(s/(n**0.5))),4)
            
            ## critical value or p-value
            c=input("""
            Enter "0" for p-value
            Enter "1" for Critical value
            """)

            if c=="0":
                self.pvalue_c(h1,n-1,test_stat)
            else:
                self.critical_t(h1,n-1)     
            
        else:
            print("enter valid option")


            
             
    def twosample_ttest_c(self):
        nm=input("""Variables name, other than \"x\" and \"y\" ??
                 Enter y or n : """)
        if nm=="y" or nm=="Y":
            var1=input("Enter your first variable name : ")
            var2=input("Enter your second variable name : ")
        else:
            var1="x"
            var2="y"
        
            
        dt=input("""
        Enter "0" for raw data
        Enter "1" for summerized data
        """)
        h1=input("""
        Type of Hypothesis
        Enter "1" for !=
        Enter "2" for <
        Enter "3" for >
        """)
        
    
        self.__display(self.__Markdown("## Two Sample-t-test :\n"))
        self.__display(self.__Math(fr"t_{{\text{{cal}}}} = \frac{{(\bar{{{var1}}} - \bar{{{var2}}})}}{{\sqrt{{\frac{{s_{var1}^2}}{{n_{var1}}} + \frac{{s_{var2}^2}}{{n_{var2}}}}}}}"))

        print(f"\nFormula :\nt_(cal)=(bar{var1}-bar{var2})/sqrt((s_{var1}^2/n_{var1})+(s_{var2}^2/n_{var2}))\n\n................................")
            
        if dt=="0":
            self.__display(self.__Markdown("### Syntax 01 :"))
            self.__display(self.__Markdown("#### (Direct calculation) :"))


            print(f"Now,\nFirst we need to calculate Mean\'s and Standard deviation\'s of {var1} and {var2},")
            print(f"\nMean of {var1} is,")
            self.Mean_c(self.__x,var1)
            print(f"\nMean of {var2} is,")
            self.Mean_c(self.__y,var2)
            
            print(f"\nStandard deviation of {var1} is,")
            self.StandardDev_S_c(self.__x,var1)
            print(f"\nStandard deviation of {var2} is,")
            self.StandardDev_S_c(self.__y,var2)
            
            nx=len(self.__x)
            ny=len(self.__y)

            mx=round(self.__st.mean(self.__x),4)
            my=round(self.__st.mean(self.__y),4)
            sx=round(self.__st.stdev(self.__x),4)
            sy=round(self.__st.stdev(self.__y),4)

            #print("\n\n")
            self.__display(self.__Markdown("## Test Statistic:\n"))
            print("\n\nNow,\nTest Statistic is,")
            print(f"\nSTEP 00 :\nt_(cal)=(bar{var1}-bar{var2})/sqrt((s_{var1}^2/n_{var1})+(s_{var2}^2/n_{var2}))")
            print(f"\nSTEP 01 :\n({mx}-{my})/sqrt(({sx}^2/{nx})+({sy}^2/{ny}))")
            print(f"\nSTEP 02 :\n({round((self.__st.mean(self.__x)-self.__st.mean(self.__y)),4)})/sqrt({round((self.__st.stdev(self.__x))**2/(nx),4)}+{round((self.__st.stdev(self.__y))**2/(ny),4)})")
            print(f"\nSTEP 03 :\n({round((self.__st.mean(self.__x)-self.__st.mean(self.__y)),4)})/sqrt({round(((self.__st.stdev(self.__x))**2/(nx))+((self.__st.stdev(self.__y))**2/(ny)),4)})")
            print(f"\nSTEP 04 :\n{round(((self.__st.mean(self.__x)-self.__st.mean(self.__y))/((((self.__st.stdev(self.__x))**2/(nx))+((self.__st.stdev(self.__y))**2/(ny)))**0.5)),4)}")
            print("\n................................\n\n")
            test_stat=round(((self.__st.mean(self.__x)-self.__st.mean(self.__y))/((((self.__st.stdev(self.__x))**2/(nx))+((self.__st.stdev(self.__y))**2/(ny)))**0.5)),4)

            # CROSS CHECK
            self.__display(self.__Markdown("## Cross check :"))
            print("Sample Covariance is :\n",self.__stats.ttest_ind(self.__x,self.__y))
            print("\n................................")
            df=len(self.__x)+len(self.__y)-2
            
        elif dt=="1":
            mx=float(input(f"{var1} bar :"))
            my=float(input(f"{var2} bar :"))
            sx=float(input(f"SD of {var1} :"))
            sy=float(input(f"SD of {var2} :"))
            nx=int(input(f"Sample size of {var1} :"))
            ny=int(input(f"Sample size of {var2} :"))
                
            self.__display(self.__Markdown("### Syntax 02 :"))
            self.__display(self.__Markdown("#### (Summarized Data) :"))


            #print("\n\n")
            self.__display(self.__Markdown("## Test Statistic:\n"))
            print("\n\nNow,\nTest Statistic is,")
            print(f"\nSTEP 00 :\nt_(cal)=(bar{var1}-bar{var2})/sqrt((s_{var1}^2/n_{var1})+(s_{var2}^2/n_{var2}))")
            print(f"\nSTEP 01 :\n({mx}-{my})/sqrt(({sx}^2/{nx})+({sy}^2/{ny}))")
            print(f"\nSTEP 02 :\n({round((mx-my),4)})/sqrt({round((sx)**2/(nx),4)}+{round((sy)**2/(ny),4)})")
            print(f"\nSTEP 03 :\n({round((mx-my),4)})/sqrt({round(((sx)**2/(nx))+((sy)**2/(ny)),4)})")
            print(f"\nSTEP 04 :\n{round(((mx-my)/((((sx)**2/(nx))+((sy)**2/(ny)))**0.5)),4)}")
            print("\n................................\n\n")
            test_stat=round(((mx-my)/((((sx)**2/(nx))+((sy)**2/(ny)))**0.5)),4)
            df=nx+ny-2
        else:
            print("enter valid option")
            
        ## critical value or p-value
        c=input("""
        Enter "0" for p-value
        Enter "1" for Critical value
        """)
        
        
        if c=="0":
            self.pvalue_c(h1,df,test_stat)
        else:
            self.critical_t(h1,df)
            

            
    def paired_ttest_c(self,before=None,after=None):
        
        dt=input("""
        Enter "0" for raw data
        Enter "1" for summerized data
        """)

    
            
        if dt=="0":

            sub=input("""How to define variable d ??
            Enter 0 for (before - after)
            Enter 1 for (after - before)""")
            
            h1=input("""
            Type of Hypothesis
            Enter "1" for !=
            Enter "2" for <
            Enter "3" for >
            """)

            var_name="d"
            self.__display(self.__Markdown("## Paired-t-test :\n"))
            self.__display(self.__Math(fr"\\t_{{cal}} = \frac{{(\bar{{{var_name}}}-\mu_{var_name})}}{{s_{var_name}/\sqrt{{n}}}}"))
            print(f"\nFormula :\nt_(cal)=({var_name}-mu_{var_name})/(s_{var_name}//sqrtn)\n\n................................")
            
            print("Now,\nFirst we need to define a variable d of difference by subtracting the both data")
            print("d=(before - after)") if sub=="0" else print("d=(after - before)")
            var=[]
            
            for i,j in zip(before,after):
                var.append(round(i-j,4)) if sub=="0" else var.append(round(j-i,4))
            self.__display(self.__Markdown("### Syntax 01 :"))
            self.__display(self.__Markdown("#### (Direct calculation) :"))
            
            string=self.__short(var)
            string=string.replace("+",",")
            string=[string]
            
            print(f"A new variable d is,\nd={string}")
            print(f"\nNow,\nFirst we need to calculate Mean and standard deviation of {var_name}")
            print(f"\nMean of {var_name} is,")
            self.Mean_c(var,var_name)
            print(f"\nStanard deviation of {var_name} is,")
            self.StandardDev_S_c(var,var_name)
            
            mu=float(input(f"Hypothetical Mean (mu) :"))
            n=len(var)

            me=round(self.__st.mean(var),4)
            s=round(self.__st.stdev(var),4)

            #print("\n\n")
            self.__display(self.__Markdown("## Test Statistic:\n"))
            print("\n\nNow,\nTest Statistic is,")
            print(f"\nSTEP 00 :\nt_(cal)=(bar{var_name}-mu_{var_name})/(s_{var_name}//sqrtn)")
            print(f"\nSTEP 01 :\n({me}-{mu})/({s}//sqrt{n})")
            print(f"\nSTEP 02 :\n({round((self.__st.mean(var)-mu),4)})/({round(self.__st.stdev(var)/(n**0.5),6)})")
            print(f"\nSTEP 03 :\n{(self.__st.mean(var)-mu)/(self.__st.stdev(var)/(n**0.5))}")
            print(f"\nSTEP 04 :\n{round(((self.__st.mean(var)-mu)/(self.__st.stdev(var)/(n**0.5))),4)}")
            print("\n................................\n\n")
            test_stat=round(((self.__st.mean(var)-mu)/(self.__st.stdev(var)/(n**0.5))),4)


            # CROSS CHECK
            self.__display(self.__Markdown("## Cross check :"))
            
            if h1=="1":
                h2="two-sided"
            elif h1=="2":
                h2="less"
            else:
                h2="greater"
            
            if sub=="0":
                print("Test Statistic is :\n",self.__stats.ttest_rel(before,after,alternative=h2))
            else:
                print("Test Statistic is :\n",self.__stats.ttest_rel(after,before,alternative=h2))
            print("\n................................")
            
            ## critical value or p-value
            c=input("""
            Enter "0" for p-value
            Enter "1" for Critical value
            """)

            if c=="0":
                self.pvalue_c(h1,len(var)-1,test_stat)
            else:
                self.critical_t(h1,len(var)-1)     
        
        elif dt=="1":
            self.onesample_ttest_c(dt="1")
            
        else:
            print("enter valid option")
            
            
#################################################
    #def Conf_
#################################################
            
            
    def critical_t(self,ht,df):
        self.__display(self.__Markdown("## Critical value :"))
        print("Now,\nTo calculate critical value we need to calculate inverse probability as,\n")
        alpha=float(input("Alpha = "))
        if ht == "1":
            critical_value = self.__stats.t.ppf(1 - alpha/2, df)
            print(f"P(absT>=t)=(1 - {alpha}/2)")
            print(f"critcal value (t_({1 - (alpha/2)})) is {round(critical_value,4)}")
        elif ht == "2":
            critical_value = self.__stats.t.ppf(alpha, df)
            print(f"P(T<t)={alpha}")
            print(f"critcal value (t_({alpha})) is {round(critical_value,4)}")
        elif ht == "3":
            critical_value = self.__stats.t.ppf(1 - alpha, df)
            print(f"P(T>t)=({alpha})")
            print(f"critcal value (t_({1 - alpha})) is {round(critical_value,4)}")
        else:
            print("Enter valid option")
            
    def pvalue_c(self,ht,df,ts):
        self.__display(self.__Markdown("## P-value :"))
        print(f"Now,\nTo calculate P-value we need to calculate probability with df={df} as,\n")
        if ht == "1":
            ts1=abs(ts)
            p1 = self.__stats.t.cdf(-ts1, df)
            print(f"P(absT>=t)=P(absT>={round(ts,4)})")
            print(f"\tP(T<-{round(ts1,4)})+P(T>{round(ts1,4)})")
            print(f"\t{round(p1,4)}+{round(p1,4)}")
            print(f"\t{round(2*p1,4)}")
            print(f"p-value is {round(2*p1,4)}")
        elif ht == "2":
            pvalue = self.__stats.t.cdf(ts, df)
            print(f"P(T<t)=P(T<{ts})")
            print(f"\t{round(pvalue,4)}")
            print(f"p-value is {round(pvalue,4)}")
        elif ht == "3":
            pvalue = self.__stats.t.cdf(ts, df)
            print(f"P(T>t)=P(T>{ts})")
            print(f"\t{round(1-pvalue,4)}")
            print(f"p-value is {round(1-pvalue,4)}")
        else:
            print("Enter valid option")
            
    def binom_c(self):
        n=int(input("n : "))
        f=int(input("from : "))
        t=int(input("to :"))
        p=float(input("P : "))

        str1=[]
        str2=[]
        str3=[]
        cal=[]
        for i in range(f,t+1):
            
            comb = self.__m.comb(n, i)
            s1=f"(({n}),({i})){p}^{i}*(1-{p})^({n}-{i})"
            s2=f"({comb})*{round(p**i,4)}*({round((1-p)**(n-i),4)})"
            s3=f"({round(comb*(p**i)*((1-p)**(n-i)),4)})"
            c=(comb*(p**i)*((1-p)**(n-i)))
            str1.append(s1)
            str2.append(s2)
            str3.append(s3)
            cal.append(c)
        print(f"\n\nStep 00:\nsum_(x={f})^({t})*((n),(x))p^x*(1-p)^(n-x)\n\n")
        print(f"Step 01:\n{self.__short(str1)}\n\n")
        print(f"Step 02:\n{self.__short(str2)}\n\n")
        print(f"Step 03:\n{self.__short(str3)}\n\n")
        print(f"Step 04:\n{round(sum(cal),4)}")



x=[97 , 82 , 123 , 92 , 175 , 88 , 118]
c=Chegg(x)
#print(len(x),len(y))


# In[6]:


# c.pvalue_c("3",2999,12.5984)
#c.Correlation_c()
# c.onesample_ttest_c(x)
# c.twosample_ttest_c()
c.StandardDev_S_c(x)
# c.paired_ttest_c()
# c.Correlation_c()
# c.Mean_c(x)
# c.Correlation_c()


# In[8]:


c.StandardDev_S_c(y)


# In[ ]:




