#pragma once


#ifdef _WIN32
  #define NODE_EXPORT __declspec(dllexport)
#else
  #define NODE_EXPORT
#endif

NODE_EXPORT void node();
