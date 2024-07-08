#include "counter.h"

// must make initialize to static data

int Counter::count = 0;

Counter::Counter()
{
    count++;
}

int Counter::getCount()
{
    return count;
}
