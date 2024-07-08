#include "rooms.h"

Rooms::Rooms(int w, int h) : width(w), height(h) {}

void Rooms::setHeight(int new_height) { height = new_height; }

int Rooms::getHeight() { return height; }

void Rooms::setWidth(int new_width) { width = new_width; }

int Rooms::getWidth() { return width; }
