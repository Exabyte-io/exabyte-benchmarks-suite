# 0. CuO SCF

Note that the SCF calculation is terminated after 4 SCF loops
(`electron_maxstep=4`), see input file `pw.cuo.scf.in` for the details.

File Name              | Description                        | Time (s)
:--------------------- | :--------------------------------- | -------:
pw.cuo.scf.gnu.0.out   | GNU Build 8 processors, 1 node     | 594.28
pw.cuo.scf.gnu.1.out   | GNU Build 16 processors, 1 node    | 488.41
pw.cuo.scf.gnu.2.out   | GNU Build 22 processors, 1 node    | 295.21
pw.cuo.scf.gnu.3.out   | GNU Build 44 processors, 1 nodes   | 212.08
pw.cuo.scf.gnu.4.out   | GNU Build 44 processors, 2 nodes   | 143.70
pw.cuo.scf.intel.0.out | Intel Build 8 processors, 1 node   | 323.41
pw.cuo.scf.intel.1.out | Intel Build 16 processors, 1 node  | 161.82
pw.cuo.scf.intel.2.out | Intel Build 22 processors, 1 node  | 138.41
pw.cuo.scf.intel.3.out | Intel Build 44 processors, 1 nodes | 79.66
pw.cuo.scf.intel.4.out | Intel Build 44 processors, 2 nodes | 42.20
pw.cuo.scf.gpu.0.out   | CUDA Build 12 processors, 1 node   | 41.81
