%nprocshared=24                                                                      
%mem=23500MB                                                                         
%chk=DAC_061222_MC_TTC_THF_Thiago.chk                                                
%rwf=/scr/guest/DAC,500GB                                                            
#p opt freq=noraman M062X/6-31g(d,p) scrf=(iefpcm,solvent=thf) scf=maxcycle=2000 maxd
                                                                                     
Estruturas que vieram da MC2                                                         
                                                                                     
0 1                                                                                                                                                                       
 C       1.497582       2.904662      -0.579039                                 
 C       1.763682       1.923092       0.482951                                 
 C       2.662482       2.244152       1.515461                                 
 C       3.302722       3.459032       1.551781                                 
 C       3.074482       4.434722       0.542031                                 
 C       2.214562       4.166312      -0.470129                                 
 H       2.860282       1.524372       2.301491                                 
 H       3.597582       5.380632       0.604291                                 
 H       2.024672       4.895022      -1.250539                                 
 N       4.211182       3.747272       2.618981                                 
 O       4.772472       4.844332       2.630961                                 
 O       4.402812       2.894382       3.487821                                 
 O       0.711922       2.698372      -1.523669                                 
 C       1.151982       0.647142       0.527811                                 
 H       1.441912       0.041072       1.379931                                 
 C       0.252822       0.128022      -0.378909                                 
 H      -0.007988       0.768692      -1.208439                                 
 C      -0.328548      -1.144588      -0.283909                                 
 C      -0.125518      -2.223248       0.782221                                 
 N      -1.196078      -1.589058      -1.203949                                 
 C      -2.538268      -3.696718      -1.604449                                 
 C      -2.791918      -4.965928      -1.087859                                 
 C      -2.177568      -5.407228       0.081441                                 
 C      -1.289958      -4.581738       0.771481                                 
 C      -1.028928      -3.320968       0.266171                                 
 C      -1.646928      -2.900878      -0.903869                                 
 H      -3.047208      -3.342938      -2.491009                                 
 H      -3.486098      -5.616978      -1.607939                                 
 H      -2.394278      -6.399598       0.461211                                 
 H      -0.815278      -4.926328       1.684551                                 
 C      -0.601248      -1.749768       2.168891                                 
 H      -1.631398      -1.389548       2.128061                                 
 H      -0.561228      -2.589228       2.866541                                 
 H       0.027372      -0.951538       2.564891                                 
 C       1.334792      -2.713238       0.821971                                 
 H       1.670692      -3.025468      -0.169139                                 
 H       2.014772      -1.944498       1.189961                                 
 H       1.404222      -3.573188       1.491781                                 
 C      -1.583198      -0.846178      -2.404449                                 
 H      -0.680148      -0.411888      -2.833779                                 
 H      -1.975508      -1.562258      -3.124319                                 
 C      -2.615698       0.245372      -2.142149                                 
 H      -2.378888       0.826102      -1.249219                                 
 H      -2.600068       0.950982      -2.979929                                 
 C      -4.028168      -0.273978      -2.048189                                 
 O      -4.418588      -1.323928      -2.507779                                 
 O      -4.833098       0.592122      -1.425409                                 
 H      -5.732758       0.224442      -1.440239                                 
 O      -2.935667       1.233132       2.469851                                 
 H      -2.238667       1.870772       2.740790                                 
 C      -3.521457       0.682732       3.647891                                 
 H      -2.799947       0.066822       4.200080                                 
 H      -3.910807       1.460402       4.319981                                 
 H      -4.350208       0.045532       3.329720                                 
 O       1.667743       0.129232      -4.113800                                 
 H       1.039513       0.884162      -4.148610                                 
 C       1.008173      -1.026258      -4.627280                                 
 H       0.184243      -1.337588      -3.972260                                 
 H       0.613253      -0.863008      -5.639920                                 
 H       1.746483      -1.831078      -4.663109                                 
 O      -0.641997       3.455402       3.676491                                 
 H      -1.436307       4.020602       3.552060                                 
 C       0.078623       3.418642       2.446361                                 
 H      -0.494007       2.901632       1.665561                                 
 H       0.338653       4.424452       2.087550                                 
 H       1.000483       2.860672       2.627990                                 
 O       2.314563      -0.458838       3.909111                                 
 H       1.653703      -0.617748       4.618930                                 
 C       3.270093      -1.517028       3.941830                                 
 H       3.862443      -1.489308       4.865551                                 
 H       2.797753      -2.505548       3.853550                                 
 H       3.943043      -1.371648       3.093251                                 
 O       4.035862      -0.199218      -2.571630                                 
 H       3.149003      -0.047708      -2.967010                                 
 C       4.673322       1.065412      -2.403759                                 
 H       4.892202       1.531962      -3.372920                                 
 H       4.066732       1.759712      -1.805379                                 
 H       5.617482       0.885342      -1.883909                                 
 O      -0.623567       1.469482      -4.798490                                 
 H      -0.453627       1.396802      -5.763730                                 
 C      -0.710897       2.852622      -4.462049                                 
 H       0.254453       3.356772      -4.599199                                 
 H      -1.471997       3.377112      -5.056779                                 
 H      -0.986817       2.911992      -3.406389                                 
 O       0.161273      -0.383938       5.394630                                 
 H       0.197423       0.526902       5.761900                                 
 C      -0.632847      -1.186808       6.265640                                 
 H      -0.147097      -1.314408       7.241661                                 
 H      -1.635117      -0.763468       6.421501                                 
 H      -0.734647      -2.168868       5.797330                                 
 O      -2.708797       4.911972       2.898751                                 
 H      -3.327167       5.376752       3.504890                                 
 C      -3.474407       4.288672       1.869581                                 
 H      -4.103018       3.484572       2.273431                                 
 H      -4.115138       5.005542       1.337021                                 
 H      -2.767497       3.853282       1.159081                                 
 O       3.577753      -4.580888      -4.223149                                 
 H       4.114872      -3.988688      -4.794630                                 
 C       3.369733      -3.928258      -2.972300                                 
 H       4.312593      -3.813778      -2.422050                                 
 H       2.907393      -2.938378      -3.092510                                 
 H       2.699453      -4.560608      -2.384979                                 
 O      -6.289398      -2.546528       2.437731                                 
 H      -7.208578      -2.270358       2.649081                                 
 C      -5.651428      -1.480578       1.737271                                 
 H      -6.111788      -1.319458       0.753921                                 
 H      -5.680798      -0.537418       2.300880                                 
 H      -4.608017      -1.769538       1.589091                                 
 O      -1.631067       7.020862      -2.313110                                 
 H      -0.981757       7.444572      -1.709199                                 
 C      -1.543967       5.607472      -2.143889                                 
 H      -0.574317       5.225012      -2.487900                                 
 H      -1.693167       5.304802      -1.097839                                 
 H      -2.330877       5.159302      -2.755470                                 
 O       0.602603      -5.334948       3.330930                                 
 H       1.582403      -5.259058       3.339441                                 
 C       0.252373      -6.657608       3.733140                                 
 H       0.581323      -7.398358       2.992910                                 
 H       0.679223      -6.920648       4.711230                                 
 H      -0.837447      -6.696668       3.802901                                 
 O       0.039353       2.342892       6.072570                                 
 H      -0.265437       2.617422       5.179501                                 
 C      -0.873187       2.863652       7.036901                                 
 H      -0.833987       3.960102       7.069700                                 
 H      -1.908497       2.552052       6.839170                                 
 H      -0.569297       2.475952       8.012341                                 
 O       3.417433      -5.555788       2.603680                                 
 H       4.376942      -5.589848       2.813520                                 
 C       3.208633      -6.211668       1.354621                                 
 H       3.679033      -5.658308       0.531601                                 
 H       3.595493      -7.240458       1.356361                                 
 H       2.130153      -6.241638       1.181271                                 
 O      -4.910997      -4.032888       4.310071                                 
 H      -5.434738      -3.512278       3.661630                                 
 C      -3.549087      -4.035268       3.886831                                 
 H      -3.426477      -4.585808       2.945170                                 
 H      -3.153227      -3.018238       3.756600                                 
 H      -2.969977      -4.541488       4.663001                                 
 O       7.591012      -0.738638       0.419971                                 
 H       8.433233      -1.220768       0.264931                                 
 C       6.513032      -1.659748       0.267101                                 
 H       6.431422      -2.007338      -0.770849                                 
 H       6.617023      -2.533288       0.926001                                 
 H       5.594402      -1.129018       0.528851                                 
 O       4.032352       5.586082      -3.969000                                 
 H       4.990582       5.458492      -4.145999                                 
 C       3.362813       4.351642      -4.217410                                 
 H       3.401893       4.085402      -5.281579                                 
 H       3.785563       3.524652      -3.629669                                 
 H       2.316913       4.487642      -3.931639                                 

