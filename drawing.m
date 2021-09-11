clc
close all
clear all
startup_rvc;
mdl_puma560
t=[1:2];

%B-------------------------------------------------------------------------
btop= readtable('btop.csv');
btop=btop{:,:};
btopx=btop(:,1)';
btopy=btop(:,2)';

bbottom= readtable('bbottom.csv');
bbottom=bbottom{:,:};
bbottomx=bbottom(:,1)';
bbottomy=bbottom(:,2)';

bbottom_c1= readtable('bbottom_c1.csv');
bbottom_c1=bbottom_c1{:,:};
bbottom_c1x=bbottom_c1(:,1)';
bbottom_c1y=bbottom_c1(:,2)';

btop_c2= readtable('btop_c2.csv');
btop_c2=btop_c2{:,:};
btop_c2x=btop_c2(:,1)';
btop_c2y=btop_c2(:,2)';

Bx=[btopx,flip(bbottom_c1x),btop_c2x,flip(bbottomx) btopx(1,1)]/1700-0.2;
By=[btopy, flip(bbottom_c1y),btop_c2y,flip(bbottomy) btopy(1,1)]/1700-0.2;

for i=1:(length(Bx)-1)
    T1=transl(Bx(i),By(i),0)*trotx(pi);
    T2=transl(Bx(i+1),By(i+1),0)*trotx(pi);
    Ts=ctraj(T1,T2,length(t));
    qs=p560.ikine6s(Ts);
    path=transl(Ts);
    p560.plot(qs,'trail',{'r', 'LineWidth', 2},'nowrist','noshadow','noarrow','zoom',5,'nobase','notiles' ,'view','top')
    hold on
    plot(path(:,1),path(:,2),'r', 'LineWidth',2)
end

bbottom_b1= readtable('bbottom_b1.csv');
bbottom_b1=bbottom_b1{:,:};
bbottomx_b1=bbottom_b1(:,1)';
bbottomy_b1=bbottom_b1(:,2)';

btop_inin= readtable('btop_inin.csv');
btop_inin=btop_inin{:,:};
btopx_inin=btop_inin(:,1)';
btopy_inin=btop_inin(:,2)';

bbottom_inin= readtable('bbottom_inin.csv');
bbottom_inin=bbottom_inin{:,:};
bbottomx_inin=bbottom_inin(:,1)';
bbottomy_inin=bbottom_inin(:,2)';

btop_b2= readtable('btop_b2.csv');
btop_b2=btop_b2{:,:};
btopx_b2=btop_b2(:,1)';
btopy_b2=btop_b2(:,2)';

Bx_inin=[bbottomx_b1  flip(btopx_inin) bbottomx_inin flip(btopx_b2) bbottomx_b1(1,1)]/1700-0.2;
By_inin=[bbottomy_b1  flip(btopy_inin) bbottomy_inin flip(btopy_b2) bbottomy_b1(1,1)]/1700-0.2;

for i=1:(length(Bx_inin)-1)
    T1=transl(Bx_inin(i),By_inin(i),0)*trotx(pi);
    T2=transl(Bx_inin(i+1),By_inin(i+1),0)*trotx(pi);
    Ts=ctraj(T1,T2,length(t));
    qs=p560.ikine6s(Ts);
    path=transl(Ts);
    p560.plot(qs,'trail',{'r', 'LineWidth', 2},'nowrist','noshadow','noarrow','nobase','notiles','zoom',5,'view','top' )
    hold on
    plot(path(:,1),path(:,2),'r', 'LineWidth',2)
end

%I-------------------------------------------------------------------------
Itop= readtable('Itop.csv');
Itop=Itop{:,:};
Itopx=Itop(:,1)';
Itopy=Itop(:,2)';

Ibottom= readtable('Ibottom.csv');
Ibottom=Ibottom{:,:};
Ibottomx=Ibottom(:,1)';
Ibottomy=Ibottom(:,2)';

Ix=[Itopx flip(Ibottomx) Itopx(1,1)]/1700-0.2;
Iy=[Itopy flip(Ibottomy) Itopy(1,1)]/1700-0.2;

for i=1:(length(Ix)-1)
    T1=transl(Ix(i),Iy(i),0)*trotx(pi);
    T2=transl(Ix(i+1),Iy(i+1),0)*trotx(pi);
    Ts=ctraj(T1,T2,length(t));
    qs=p560.ikine6s(Ts);
    path=transl(Ts);
    p560.plot(qs,'trail',{'r', 'LineWidth', 2},'nowrist','noshadow','noarrow','zoom',5,'nobase','view','top')
    hold on
    plot(path(:,1),path(:,2),'r', 'LineWidth', 2)
end

%leaf----------------------------------------------------------------------
gtop= readtable('gtop.csv');
gtop=gtop{:,:};
gtopx=gtop(:,1)';
gtopy=gtop(:,2)';

gbottom= readtable('gbottom.csv');
gbottom=gbottom{:,:};
gbottomx=gbottom(:,1)';
gbottomy=gbottom(:,2)';

Gx=[gtopx flip(gbottomx) gtopx(1,1)]/1700-0.2;
Gy=[gtopy flip(gbottomy) gtopy(1,1)]/1700-0.2;

for i=1:(length(Gx)-1)
    T1=transl(Gx(i),Gy(i),0)*trotx(pi);
    T2=transl(Gx(i+1),Gy(i+1),0)*trotx(pi);
    Ts=ctraj(T1,T2,length(t));
    qs=p560.ikine6s(Ts);
    path=transl(Ts);
    p560.plot(qs,'trail',{'green', 'LineWidth', 2},'nowrist','noshadow','noarrow','zoom',5,'nobase','notiles' ,'view','top')
    hold on
    plot(path(:,1),path(:,2),'green', 'LineWidth', 2)
end

%L-------------------------------------------------------------------------
ltop= readtable('ltop.csv');
ltop=ltop{:,:};
ltopx=ltop(:,1)';
ltopy=ltop(:,2)';

lbottom= readtable('lbottom.csv');
lbottom=lbottom{:,:};
lbottomx=lbottom(:,1)';
lbottomy=lbottom(:,2)';

Lx=[ltopx flip(lbottomx) ltopx(1,1)]/1700-0.2;
Ly=[ltopy flip(lbottomy) ltopy(1,1)]/1700-0.2;

for i=1:(length(Lx)-1)
    T1=transl(Lx(i),Ly(i),0)*trotx(pi);
    T2=transl(Lx(i+1),Ly(i+1),0)*trotx(pi);
    Ts=ctraj(T1,T2,length(t));
    qs=p560.ikine6s(Ts);
    path=transl(Ts);
    p560.plot(qs,'trail',{'r', 'LineWidth', 2},'nowrist','noshadow','noarrow','zoom',5,'nobase','notiles' ,'view','top')
    hold on
    plot(path(:,1),path(:,2),'r', 'LineWidth', 2)
end

%O-------------------------------------------------------------------------
otop= readtable('otop.csv');
otop=otop{:,:};
otopx=otop(:,1)';
otopy=otop(:,2)';

obottom= readtable('obottom.csv');
obottom=obottom{:,:};
obottomx=obottom(:,1)';
obottomy=obottom(:,2)';

Ox=[otopx flip(obottomx) otopx(1,1)]/1700-0.2;
Oy=[otopy flip(obottomy) otopy(1,1)]/1700-0.2;


for i=1:(length(Ox)-1)
    T1=transl(Ox(i),Oy(i),0)*trotx(pi);
    T2=transl(Ox(i+1),Oy(i+1),0)*trotx(pi);
    Ts=ctraj(T1,T2,length(t));
    qs=p560.ikine6s(Ts);
    path=transl(Ts);
    p560.plot(qs,'trail',{'r', 'LineWidth', 2},'nowrist','noshadow','noarrow','zoom',5,'nobase','notiles' ,'view','top')
    hold on
    plot(path(:,1),path(:,2),'r', 'LineWidth', 2')

end

Obottom_o1= readtable('Obottom_o1.csv');
Obottom_o1=Obottom_o1{:,:};
Obottomx_o1=Obottom_o1(:,1)';
Obottomy_o1=Obottom_o1(:,2)';

Otop_o1= readtable('Otop_o1.csv');
Otop_o1=Otop_o1{:,:};
Otopx_o1=Otop_o1(:,1)';
Otopy_o1=Otop_o1(:,2)';

Ox_inin=[Obottomx_o1 flip(Otopx_o1) Obottomx_o1(1,1)]/1700-0.2;
Oy_inin=[Obottomy_o1 flip(Otopy_o1) Obottomy_o1(1,1)]/1700-0.2;

for i=1:(length(Ox_inin)-1)
    T1=transl(Ox_inin(i),Oy_inin(i),0)*trotx(pi);
    T2=transl(Ox_inin(i+1),Oy_inin(i+1),0)*trotx(pi);
    Ts=ctraj(T1,T2,length(t));
    qs=p560.ikine6s(Ts);
    path=transl(Ts);
    p560.plot(qs,'trail',{'r', 'LineWidth', 2},'nowrist','noshadow','noarrow','zoom',5,'nobase','notiles','view','top' )
    hold on
    plot(path(:,1),path(:,2),'r', 'LineWidth', 2')

end
















