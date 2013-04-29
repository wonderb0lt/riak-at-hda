{
    schema,
    [
        {version, "1.2"},
        %%{default_field, "title"},
        {default_op, "or"},
        {n_val, 3},
        {analyzer_factory, {erlang, text_analyzers, whitespace_analyzer_factory}}
    ],
    [


        {field, [
            {name, "id"}, %% What is to say against id? We already know this is a passenger...
            %% Alternative to the key = id, we could use for example PFEIFFER/ELKEMS here.
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "surname"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "name"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "type"}, %% i.e. adult, child etc. (0 = Adult, 1 = Child, 2 = Infant)
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, integer}
        ]},

        {dynamic_field, [
            {name, "*"}
        ]}
    ]
}.
