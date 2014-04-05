############################################################
# Set up vim for puppet module development                 #
# Mick England <england.mick@gmail.com>                    #
# March 9, 20014                                           #
############################################################

declare -a directories=('bundle' 'autoload')
for dir in "${directories[@]}"
do
    if [ ! -d ~/.vim/$dir ]; then
        mkdir ~/.vim/$dir
    else
        echo "Directory ${dir} exists."
    fi
done

if grep "pathogen#infect()" ~/.vimrc; then
    echo "Looks like pathogen is already setup."
else
    cat "pathogen#infect()" >> ~/.vimrc
    fi

if 


