#ifndef SEMANTIC_H
#define SEMANTIC_H

#include "structs/types.h"

void semAdd    ();
void semSub    ();
void semMul    ();
void semDiv    ();
void semMod    ();
void semWrite  (Etype);
void semWritei ();
void semWritef ();
void semWrites ();
void semNot    ();
void semInf    ();
void semInfeq  ();
void semSup    ();
void semSupeq  ();
void semEq     ();
void semDif    ();
void semFadd   ();
void semFsub   ();
void semFmul   ();
void semFdiv   ();
void semFcos   ();
void semFsin   ();
void semFtan   ();
void semFinf   ();
void semFinfeq ();
void semFsup   ();
void semFsupeq ();
void semFeq    ();
void semFdif   ();
void semPadd   ();
void semConcat ();
void semAlloc  ();
void semAllocn ();
void semFree   ();
void semEqual  ();
void semAtoi   ();
void semAtof   ();
void semItof   ();
void semFtoi   ();
void semStri   ();
void semStrf   ();
void semPushi  (Value);
void semPushn  ();
void semPushf  (Value);
void semPushs  ();
void semPushg  ();
void semPushl  ();
void semPushsp ();
void semPushfp ();
void semPushgp ();
void semLoad   ();
void semLoadn  ();
void semDup    ();
void semDupn   ();
void semPop    ();
void semPopn   ();
void semStorel ();
void semStoreg ();
void semStore  ();
void semStoren ();
void semCheck  ();
void semSwap   ();
void semRead   ();
void semReadi  ();
void semReadf  ();
void semReads  ();
void semJump   ();
void semJz     ();
void semPusha  ();
void semCall   ();
void semReturn ();
void semStart  ();
void semNop    ();
void semErr    ();
void semStop   ();
void semLabel  ();

#endif