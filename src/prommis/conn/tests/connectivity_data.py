import pytest

@pytest.fixture
def uky_csv():
    return [
        "Arcs,leach_mixer,leach,leach_liquid_feed,sl_sep1,leach_solid_feed,precipitator,sl_sep2,leach_sx_mixer,leach_filter_cake_liquid,leach_filter_cake,precip_sep,precip_purge,precip_sx_mixer,roaster,solex_cleaner_load,solex_cleaner_strip,cleaner_mixer,cleaner_org_make_up,acid_feed3,cleaner_sep,cleaner_purge,solex_rougher_load,load_sep,solex_rougher_scrub,rougher_mixer,rougher_org_make_up,acid_feed1,scrub_sep,solex_rougher_strip,acid_feed2,rougher_sep,sc_circuit_purge",
        "leaching_feed_mixture,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "leaching_liq_feed,1,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "leaching_liquid_outlet,0,-1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "leaching_sol_feed,0,1,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "leaching_solid_outlet,0,-1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "precip_aq_outlet,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "precip_solid_outlet,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sl_sep1_liquid_outlet,0,0,0,-1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sl_sep1_retained_liquid_outlet,0,0,0,-1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sl_sep1_solid_outlet,0,0,0,-1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sl_sep2_aq_purge,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sl_sep2_aq_recycle,0,0,0,0,0,0,0,0,0,0,-1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sl_sep2_liquid_outlet,0,0,0,0,0,0,-1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sl_sep2_retained_liquid_outlet,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sl_sep2_solid_outlet,0,0,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_load_aq_feed,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_load_aq_outlet,0,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_load_org_outlet,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_mixed_org_recycle,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_org_feed,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_strip_acid_feed,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_strip_aq_outlet,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_strip_org_outlet,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_strip_org_purge,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0",
        "sx_cleaner_strip_org_recycle,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0",
        "sx_rougher_load_aq_feed,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0",
        "sx_rougher_load_aq_outlet,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0",
        "sx_rougher_load_aq_recycle,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0",
        "sx_rougher_load_org_outlet,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,1,0,0,0,0,0,0,0,0",
        "sx_rougher_mixed_org_recycle,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,-1,0,0,0,0,0,0,0",
        "sx_rougher_org_feed,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0",
        "sx_rougher_scrub_acid_feed,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,-1,0,0,0,0,0",
        "sx_rougher_scrub_aq_outlet,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,1,0,0,0,0",
        "sx_rougher_scrub_aq_recycle,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0",
        "sx_rougher_scrub_org_outlet,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,1,0,0,0",
        "sx_rougher_strip_acid_feed,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0",
        "sx_rougher_strip_aq_outlet,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0",
        "sx_rougher_strip_org_outlet,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,1,0",
        "sx_rougher_strip_org_purge,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1",
        "sx_rougher_strip_org_recycle,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,-1,0",
    ]


@pytest.fixture
def uky_mermaid():
    return [
        "flowchart LR",
        "   Unit_B[leach_mixer]",
        "   Unit_C[leach]",
        "   Unit_D[leach_liquid_feed]",
        "   Unit_E[sl_sep1]",
        "   Unit_F[leach_solid_feed]",
        "   Unit_G[precipitator]",
        "   Unit_H[sl_sep2]",
        "   Unit_I[leach_sx_mixer]",
        "   Unit_J[leach_filter_cake_liquid]",
        "   Unit_K[leach_filter_cake]",
        "   Unit_L[precip_sep]",
        "   Unit_M[precip_purge]",
        "   Unit_N[precip_sx_mixer]",
        "   Unit_O[roaster]",
        "   Unit_P[solex_cleaner_load]",
        "   Unit_Q[solex_cleaner_strip]",
        "   Unit_R[cleaner_mixer]",
        "   Unit_S[cleaner_org_make_up]",
        "   Unit_T[acid_feed3]",
        "   Unit_U[cleaner_sep]",
        "   Unit_V[cleaner_purge]",
        "   Unit_W[solex_rougher_load]",
        "   Unit_X[load_sep]",
        "   Unit_Y[solex_rougher_scrub]",
        "   Unit_Z[rougher_mixer]",
        "   Unit_AA[rougher_org_make_up]",
        "   Unit_AB[acid_feed1]",
        "   Unit_AC[scrub_sep]",
        "   Unit_AD[solex_rougher_strip]",
        "   Unit_AE[acid_feed2]",
        "   Unit_AF[rougher_sep]",
        "   Unit_AG[sc_circuit_purge]",
        "   Unit_AG --> Unit_C",
        "   Unit_AG --> Unit_B",
        "   Unit_AG --> Unit_E",
        "   Unit_AG --> Unit_C",
        "   Unit_AG --> Unit_E",
        "   Unit_AG --> Unit_H",
        "   Unit_AG --> Unit_H",
        "   Unit_AG --> Unit_I",
        "   Unit_AG --> Unit_J",
        "   Unit_AG --> Unit_K",
        "   Unit_AG --> Unit_M",
        "   Unit_AG --> Unit_N",
        "   Unit_AG --> Unit_L",
        "   Unit_AG --> Unit_O",
        "   Unit_AG --> Unit_O",
        "   Unit_AG --> Unit_P",
        "   Unit_AG --> Unit_I",
        "   Unit_AG --> Unit_Q",
        "   Unit_AG --> Unit_P",
        "   Unit_AG --> Unit_R",
        "   Unit_AG --> Unit_Q",
        "   Unit_AG --> Unit_G",
        "   Unit_AG --> Unit_U",
        "   Unit_AG --> Unit_V",
        "   Unit_AG --> Unit_R",
        "   Unit_AG --> Unit_W",
        "   Unit_AG --> Unit_X",
        "   Unit_AG --> Unit_B",
        "   Unit_AG --> Unit_Y",
        "   Unit_AG --> Unit_W",
        "   Unit_AG --> Unit_Z",
        "   Unit_AG --> Unit_Y",
        "   Unit_AG --> Unit_AC",
        "   Unit_AG --> Unit_B",
        "   Unit_AG --> Unit_AD",
        "   Unit_AG --> Unit_AD",
        "   Unit_AG --> Unit_N",
        "   Unit_AG --> Unit_AF",
        "   Unit_AF --> Unit_AG",
        "   Unit_AG --> Unit_Z",
        "",
    ]
