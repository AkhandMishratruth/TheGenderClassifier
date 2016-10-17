path='H:\projects and exp\FACE classifier\Men Resize\'
female=zeros(291,1600);
for i=1:291
    name=strcat(path,int2str(i),'.jpg');
    temp=imread(name);
    temp=rgb2gray(temp);
    temp=(temp(:))';
    female(i,:)=temp;
end
    
    