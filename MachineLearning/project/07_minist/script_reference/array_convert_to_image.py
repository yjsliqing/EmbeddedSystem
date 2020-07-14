import numpy as np
from matplotlib import pyplot as plt

image = [38,64,17,39,65,20,41,66,27,37,61,27,34,54,27,39,59,34,48,66,42,46,64,38,31,50,22,52,71,39,57,78,45,47,71,37,62,86,54,88,113,84,86,111,89,62,87,68,43,70,55,70,97,82,61,83,70,54,77,59,88,107,88,87,108,89,61,83,70,61,87,76,37,63,60,24,52,53,27,55,59,55,80,87,52,69,77,29,42,50,33,42,49,27,34,40,125,152,101,119,145,98,114,137,95,105,127,91,97,113,84,93,109,82,94,108,82,92,105,79,82,95,65,99,113,80,116,132,96,126,143,107,135,155,120,142,163,132,136,159,133,125,147,126,114,137,119,111,132,117,84,102,86,80,97,79,115,130,111,115,129,112,67,85,73,36,56,47,39,61,59,26,50,52,29,52,58,57,77,84,44,61,68,17,28,34,24,31,37,25,33,36,182,207,150,178,203,148,178,200,153,181,197,158,180,191,157,174,181,150,168,173,143,168,168,140,163,164,132,168,170,133,181,185,148,194,202,163,194,204,167,181,195,159,175,190,159,178,192,166,182,197,176,151,164,146,113,124,107,111,120,103,145,149,132,155,159,145,115,120,113,69,78,73,46,57,59,39,54,59,45,62,69,69,86,93,51,64,70,20,30,32,28,34,34,30,36,34,186,211,146,191,215,155,202,219,167,213,225,179,217,222,182,208,205,172,198,189,158,197,184,152,203,189,154,205,191,154,210,201,160,216,211,169,218,216,175,213,215,175,211,215,180,212,217,185,216,221,198,180,183,162,145,146,128,128,125,108,125,118,102,122,114,103,93,86,80,49,45,44,40,39,44,44,49,55,55,62,70,72,81,86,57,65,68,40,46,44,49,54,48,46,49,42,195,218,148,202,223,156,200,214,155,194,198,148,188,181,139,172,156,122,159,136,104,161,132,100,174,144,108,195,165,127,214,186,146,226,203,159,241,224,180,253,242,197,246,239,197,229,223,187,208,203,174,165,157,134,119,106,87,81,64,48,58,36,23,62,37,30,64,40,40,48,27,32,34,18,28,40,30,41,40,37,46,49,50,55,49,51,50,61,64,57,91,93,80,87,90,73,199,221,148,208,225,155,186,196,135,149,147,96,130,115,74,120,94,59,122,86,54,134,91,59,140,94,61,178,132,96,213,169,130,228,189,146,246,215,169,254,230,184,233,211,170,194,176,138,126,109,79,113,93,68,106,81,61,101,72,56,99,62,53,97,58,53,86,47,50,64,29,36,55,27,39,45,23,35,31,18,28,36,30,34,46,43,38,77,78,64,139,138,118,160,160,136,190,211,136,205,220,151,177,181,122,120,112,63,96,72,34,100,64,32,120,70,43,143,86,59,147,86,57,185,122,89,211,153,116,216,163,123,218,173,131,219,180,137,192,157,119,155,122,87,130,101,71,129,99,73,128,91,72,128,86,70,133,85,75,128,77,74,115,64,69,104,57,67,96,56,67,60,30,42,36,15,22,50,38,38,57,48,39,81,76,57,157,156,128,213,212,181,186,203,132,210,222,156,181,182,125,116,103,58,89,60,26,99,55,30,124,66,46,151,84,65,171,99,77,195,121,96,206,137,106,201,137,102,196,138,101,194,142,105,179,133,97,161,118,84,151,112,83,153,113,88,141,94,74,127,76,59,126,69,58,123,64,60,123,64,68,133,77,86,120,74,85,67,31,41,40,15,19,66,51,48,65,53,39,66,60,36,148,143,111,226,222,185,188,205,137,205,215,154,165,163,112,83,68,27,78,44,17,113,66,48,130,68,55,161,89,77,190,112,99,179,100,83,173,95,73,174,100,73,179,112,83,187,126,95,181,126,95,165,114,85,150,100,75,150,100,77,141,89,68,149,92,75,129,67,56,117,52,46,143,79,80,126,70,73,114,67,73,72,36,40,36,10,11,57,40,33,62,49,33,51,44,18,135,129,95,246,241,203,193,209,147,200,211,153,136,135,89,65,49,15,66,34,13,96,48,36,124,64,56,155,84,78,184,105,98,165,83,71,157,78,61,171,94,74,181,109,85,182,116,90,181,119,94,176,118,94,145,88,68,144,87,67,147,89,69,168,107,89,150,84,70,123,59,50,136,75,70,124,68,67,107,63,62,52,18,16,40,15,11,83,66,56,77,64,45,64,54,27,142,134,98,228,220,181,190,207,152,190,203,150,102,103,63,48,37,7,57,30,11,74,31,22,114,59,56,143,78,76,166,93,87,141,64,56,138,60,48,161,85,69,173,102,82,172,106,84,174,112,91,180,119,100,139,80,62,138,79,61,154,93,74,184,121,103,169,106,89,133,74,60,128,74,62,117,70,60,87,50,41,56,28,17,40,20,9,73,60,44,79,68,46,70,61,32,137,129,93,220,210,174,184,202,150,187,201,152,85,89,52,43,36,8,55,34,17,57,23,14,106,58,56,136,78,77,138,73,69,124,53,47,125,52,43,145,73,59,158,89,73,164,97,78,169,104,86,170,107,90,135,73,58,138,76,61,158,97,79,184,123,105,175,117,97,147,92,72,124,77,57,103,66,47,62,35,16,99,81,61,64,51,32,44,36,15,68,61,35,69,62,33,121,110,78,213,203,168,186,206,155,192,210,162,88,96,59,37,35,10,45,32,16,48,21,14,98,60,59,135,87,87,111,56,53,113,52,47,120,56,46,129,63,49,139,74,56,155,90,70,160,97,79,152,89,72,120,58,47,128,66,55,153,91,78,167,110,91,167,112,91,147,101,75,114,77,48,89,62,33,90,73,45,163,153,126,121,115,89,49,45,20,48,44,19,67,60,34,126,115,87,208,194,165,191,214,162,201,220,174,100,112,76,25,29,4,30,23,7,43,24,17,83,55,52,123,85,84,93,48,43,105,55,46,114,60,48,115,58,41,119,61,41,140,79,60,150,89,70,141,79,64,105,45,35,109,49,41,132,74,62,138,85,67,138,91,65,131,92,59,109,81,44,105,90,51,180,172,135,217,217,181,173,177,144,85,88,57,36,35,7,61,55,29,150,141,112,215,204,176,186,210,158,201,223,176,115,129,93,18,27,0,22,21,1,44,34,22,56,37,31,87,59,55,87,53,43,96,56,44,105,59,44,106,57,40,107,55,34,120,65,44,136,80,63,141,85,72,115,56,50,94,37,30,103,49,37,101,52,35,98,59,30,100,70,32,116,97,54,168,162,114,229,231,184,233,242,197,201,212,170,151,159,122,91,95,62,70,69,38,138,131,102,210,201,170,177,199,150,198,217,171,126,142,106,20,29,0,22,26,3,48,45,28,32,19,10,49,31,21,85,62,46,84,55,37,91,58,39,99,61,42,95,54,34,101,56,37,123,77,62,143,95,85,131,80,76,86,35,31,79,31,19,70,29,9,66,33,2,75,53,12,128,118,69,230,230,176,205,214,159,219,233,180,210,227,175,218,231,185,182,190,149,91,96,56,94,94,56,176,174,136,179,196,151,182,199,155,100,114,81,10,19,0,83,87,62,137,136,115,26,20,6,75,66,51,142,130,106,97,81,56,61,40,19,62,36,19,70,43,24,77,48,32,105,71,61,140,103,97,164,123,121,105,62,56,62,22,10,58,26,5,66,43,11,55,42,0,179,177,126,221,229,170,204,218,156,219,238,174,208,226,164,215,233,173,216,233,178,140,154,101,114,124,74,193,203,153,195,212,167,161,178,136,53,67,34,31,42,12,131,140,109,141,147,119,32,34,13,89,88,67,200,199,168,127,123,88,53,46,18,33,21,0,45,30,7,59,42,22,74,55,41,91,66,59,102,71,68,90,57,50,61,32,18,44,22,0,60,45,12,105,101,56,205,210,156,221,235,173,218,238,169,220,241,172,216,239,169,228,251,183,231,253,188,194,216,152,182,202,141,217,237,178,197,219,170,134,156,110,7,24,0,67,82,49,177,192,153,116,128,92,26,36,9,109,118,89,218,227,184,178,186,139,126,131,91,84,86,49,57,57,21,49,46,15,61,55,31,82,69,53,122,102,93,112,90,79,62,45,29,42,30,4,72,68,33,168,171,126,213,226,170,211,232,167,205,231,160,199,227,153,207,235,161,215,243,169,207,237,165,205,235,165,210,237,170,207,233,168,186,213,160,122,148,100,3,25,0,107,129,90,191,213,167,72,91,46,17,32,0,135,151,114,192,209,157,203,218,163,200,214,165,175,187,141,145,154,107,135,144,99,157,161,126,184,182,157,202,193,176,141,129,115,41,34,15,34,33,5,93,97,60,205,217,169,202,221,165,203,228,163,202,232,160,200,232,157,212,244,168,213,245,170,197,229,154,198,230,157,205,236,166,197,228,160,187,216,160,126,155,101,30,57,12,145,172,129,196,222,174,59,85,37,24,47,5,159,181,135,198,222,162,199,221,157,196,217,158,193,213,154,199,219,158,212,232,173,225,239,190,229,239,202,235,237,213,149,148,130,17,19,0,18,24,0,107,119,79,217,237,186,197,222,164,204,234,170,194,230,158,196,234,159,200,237,160,203,240,163,203,239,165,197,230,159,193,226,155,198,231,160,195,224,168,119,149,95,63,92,46,167,196,150,201,229,180,89,117,66,43,70,25,166,193,142,197,226,160,191,221,151,187,213,148,189,215,150,199,226,155,208,235,166,207,231,171,202,219,174,226,237,207,165,173,150,31,41,17,14,27,0,120,138,98,208,232,182,197,226,168,195,230,164,178,215,145,177,217,144,171,209,134,180,218,143,203,239,165,197,233,161,185,218,147,193,226,155,191,218,165,90,118,69,77,104,59,167,194,149,188,216,167,109,137,88,39,66,21,147,175,124,170,201,133,177,209,136,187,218,150,194,225,157,195,229,153,197,229,154,200,230,166,207,231,181,210,227,193,170,184,159,40,56,30,14,33,3,136,158,119,182,210,161,187,221,161,180,216,152,180,220,149,185,225,152,179,217,142,177,215,140,192,228,154,193,229,155,187,220,149,189,222,151,177,201,153,57,83,36,78,103,63,157,182,142,167,193,146,105,133,85,18,45,2,122,152,102,171,202,135,162,196,122,158,190,123,164,197,128,173,207,131,178,212,136,182,214,149,186,214,163,189,211,175,144,163,135,16,35,7,4,25,0,146,171,131,160,188,139,179,212,155,177,212,148,184,221,152,197,235,162,197,233,161,177,213,139,165,198,127,170,203,132,176,207,137,172,203,133,162,183,140,44,67,25,61,83,47,152,174,138,180,203,161,105,130,88,36,61,22,89,116,71,155,183,124,154,185,118,152,182,118,151,181,117,160,191,121,174,205,135,178,208,148,175,203,154,153,175,139,51,71,43,16,36,8,10,31,0,137,162,120,172,200,151,186,215,161,156,187,127,176,208,143,191,223,156,195,228,159,184,217,146,178,209,141,181,212,144,179,208,141,168,197,130,146,167,126,55,76,37,74,93,61,144,163,131,162,184,146,98,120,82,24,48,14,56,81,41,147,174,119,153,181,120,151,179,121,151,181,121,167,198,131,175,205,141,146,175,119,105,131,86,44,66,30,58,79,48,70,91,58,34,56,18,131,156,114,152,178,130,176,205,151,195,224,166,168,198,136,180,210,146,189,218,152,186,215,149,184,213,147,186,215,149,185,211,146,179,205,140,137,158,117,82,103,64,98,117,85,134,153,123,145,167,131,108,130,94,50,71,40,59,81,45,126,150,100,143,171,113,151,178,125,149,176,123,157,186,128,153,182,124,99,125,77,31,56,16,32,54,18,102,123,90,100,122,86,35,57,18,138,164,119,168,194,146,168,195,142,193,221,163,177,205,146,183,211,150,192,218,157,196,222,159,195,221,158,189,215,152,182,210,149,179,207,146,136,159,115,111,133,94,116,137,104,120,141,108,128,152,116,128,152,116,100,123,94,98,122,86,110,136,88,134,161,108,150,176,128,145,173,124,137,166,112,118,146,95,72,97,55,21,46,7,95,119,83,141,166,127,96,121,81,20,45,3,129,155,108,180,208,159,167,194,141,177,204,149,196,224,166,192,220,161,195,223,164,201,229,170,196,224,165,182,210,151,171,200,142,169,198,140,132,162,112,127,156,110,125,153,113,115,143,105,122,150,110,139,167,127,134,159,127,128,154,117,126,154,105,137,166,112,148,176,128,146,175,129,134,164,114,114,143,95,90,116,77,72,98,61,120,146,107,144,171,128,107,134,89,45,73,25,105,133,84,154,184,132,162,191,137,185,214,158,188,217,161,180,211,152,179,210,151,183,217,157,179,212,155,164,197,140,154,187,130,154,187,130,134,169,113,138,173,119,137,170,125,133,166,123,135,
168,123,140,173,130,139,169,133,132,163,122,143,175,125,141,174,119,141,173,124,145,176,132,144,176,129,136,167,123,130,158,120,126,154,116,139,167,126,142,174,127,131,163,114,103,135,85,115,148,95,145,178,125,151,184,129,169,202,147,157,190,133,149,182,125,146,181,123,150,188,131,153,191,134,148,186,129,142,180,123,141,179,122,124,166,102,126,168,105,130,170,117,143,183,133,142,182,130,127,167,117,125,162,119,124,161,117,120,157,103,127,165,108,132,169,118,134,170,124,139,172,125,144,177,132,143,175,136,138,170,131,153,186,143,144,177,130,145,179,128,143,178,124,140,175,121,159,194,138,148,183,127,148,183,127,138,176,119,133,171,114,126,165,108,129,168,113,135,176,120,138,179,123,135,178,122,132,175,119,102,147,78,100,145,80,106,149,93,133,176,123,133,176,122,108,151,98,109,148,104,115,154,107,80,119,64,109,148,91,127,165,114,121,159,112,120,156,108,130,166,120,133,167,130,125,160,120,131,164,121,132,166,116,143,180,128,151,188,134,139,174,118,159,194,138,150,188,131,160,198,141,142,181,124,136,175,118,127,168,112,124,165,109,128,171,115,136,179,123,134,179,124,128,173,118]

a=np.array(image).reshape(32,32,3)

plt.imshow(a)
plt.show()