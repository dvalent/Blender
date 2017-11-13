

class ops:
    '''Spcecial class, created just to reflect content of bpy.ops'''

    class action:
        '''Spcecial class, created just to reflect content of bpy.ops.action'''

        def clean(threshold=0.001, channels=False):
            '''Simplify F-Curves by removing closely spaced keyframes
               Arguments:
               @threshold (float): in [0, inf], (optional)
               @channels (bool): (optional)

            '''

            pass

        def clickselect(extend=False, column=False, channel=False):
            '''Select keyframes by clicking on them
               Arguments:
               @extend (bool): Toggle keyframe selection instead of leaving newly selected keyframes only
                  (optional)
               @column (bool): Select all keyframes that occur on the same frame as the one under the mouse
                  (optional)
               @channel (bool): Select all the keyframes in the channel under the mouse
                  (optional)

            '''

            pass

        def copy():
            '''Copy selected keyframes to the copy/paste buffer
            '''

            pass

        def delete():
            '''Remove all selected keyframes
            '''

            pass

        def duplicate():
            '''Make a copy of all selected keyframes
            '''

            pass

        def duplicate_move(ACTION_OT_duplicate=None, TRANSFORM_OT_transform=None):
            '''Make a copy of all selected keyframes and move them
               Arguments:
               @ACTION_OT_duplicate (ACTION_OT_duplicate): Make a copy of all selected keyframes
                  (optional)
               @TRANSFORM_OT_transform (TRANSFORM_OT_transform): Transform selected items by mode type
                  (optional)

            '''

            pass

        def extrapolation_type(type='CONSTANT'):
            '''Set extrapolation mode for selected F-Curves
               Arguments:
               @type (str): in ['CONSTANT', 'LINEAR', 'MAKE_CYCLIC', 'CLEAR_CYCLIC'], (optional)

            '''

            pass

        def frame_jump():
            '''Set the current frame to the average frame value of selected keyframes
            '''

            pass

        def handle_type(type='FREE'):
            '''Set type of handle for selected keyframes
               Arguments:
               @type (str): in ['FREE', 'VECTOR', 'ALIGNED', 'AUTO', 'AUTO_CLAMPED'], (optional)

            '''

            pass

        def interpolation_type(type='CONSTANT'):
            '''Set interpolation mode for the F-Curve segments starting from the selected keyframes
               Arguments:
               @type (str): in ['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC'], (optional)

            '''

            pass

        def keyframe_insert(type='ALL'):
            '''Insert keyframes for the specified channels
               Arguments:
               @type (str): in ['ALL', 'SEL', 'GROUP'], (optional)

            '''

            pass

        def keyframe_type(type='KEYFRAME'):
            '''Set type of keyframe for the selected keyframes
               Arguments:
               @type (str): in ['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER'], (optional)

            '''

            pass

        def layer_next():
            '''Switch to editing action in animation layer above the current action in the NLA Stack
            '''

            pass

        def layer_prev():
            '''Switch to editing action in animation layer below the current action in the NLA Stack
            '''

            pass

        def markers_make_local():
            '''Move selected scene markers to the active Action as local 'pose' markers
            '''

            pass

        def mirror(type='CFRA'):
            '''Flip selected keyframes over the selected mirror line
               Arguments:
               @type (str): in ['CFRA', 'XAXIS', 'MARKER'], (optional)

            '''

            pass

        def new():
            '''Create new action
            '''

            pass

        def paste(offset='START', merge='MIX', flipped=False):
            '''Paste keyframes from copy/paste buffer for the selected channels, starting on the current frame
               Arguments:
               @offset (str): Paste time offset of keys
                  in ['START', 'END', 'RELATIVE', 'NONE'], (optional)
               @merge (str): Method of merging pasted keys and existing
                  in ['MIX', 'OVER_ALL', 'OVER_RANGE', 'OVER_RANGE_ALL'], (optional)
               @flipped (bool): Paste keyframes from mirrored bones if they exist
                  (optional)

            '''

            pass

        def previewrange_set():
            '''Set Preview Range based on extents of selected Keyframes
            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def push_down():
            '''Push action down on to the NLA stack as a new strip
            '''

            pass

        def sample():
            '''Add keyframes on every frame between the selected keyframes
            '''

            pass

        def select_all_toggle(invert=False):
            '''Toggle selection of all keyframes
               Arguments:
               @invert (bool): (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False):
            '''Select all keyframes within the specified region
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @axis_range (bool): (optional)

            '''

            pass

        def select_circle(x=0, y=0, radius=1, gesture_mode=0):
            '''Select keyframe points using circle selection
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @radius (int): in [1, inf], (optional)
               @gesture_mode (int): in [-inf, inf], (optional)

            '''

            pass

        def select_column(mode='KEYS'):
            '''Select all keyframes on the specified frame(s)
               Arguments:
               @mode (str): in ['KEYS', 'CFRA', 'MARKERS_COLUMN', 'MARKERS_BETWEEN'], (optional)

            '''

            pass

        def select_lasso(path=None, deselect=False, extend=True):
            '''Select keyframe points using lasso selection
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @deselect (bool): Deselect rather than select items
                  (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_leftright(mode='CHECK', extend=False):
            '''Select keyframes to the left or the right of the current frame
               Arguments:
               @mode (str): in ['CHECK', 'LEFT', 'RIGHT'], (optional)
               @extend (bool): (optional)

            '''

            pass

        def select_less():
            '''Deselect keyframes on ends of selection islands
            '''

            pass

        def select_linked():
            '''Select keyframes occurring in the same F-Curves as selected ones
            '''

            pass

        def select_more():
            '''Select keyframes beside already selected ones
            '''

            pass

        def snap(type='CFRA'):
            '''Snap selected keyframes to the times specified
               Arguments:
               @type (str): in ['CFRA', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER'], (optional)

            '''

            pass

        def stash(create_new=True):
            '''Store this action in the NLA stack as a non-contributing strip for later use
               Arguments:
               @create_new (bool): Create a new action once the existing one has been safely stored
                  (optional)

            '''

            pass

        def stash_and_create():
            '''Store this action in the NLA stack as a non-contributing strip for later use, and create a new action
            '''

            pass

        def unlink(force_delete=False):
            '''Unlink this action from the active action slot (and/or exit Tweak Mode)
               Arguments:
               @force_delete (bool): Clear Fake User and remove copy stashed in this datablock's NLA stack
                  (optional)

            '''

            pass

        def view_all():
            '''Reset viewable area to show full keyframe range
            '''

            pass

        def view_frame():
            '''Reset viewable area to show range around current frame
            '''

            pass

        def view_selected():
            '''Reset viewable area to show selected keyframes range
            '''

            pass

    class anim:
        '''Spcecial class, created just to reflect content of bpy.ops.anim'''

        def change_frame(frame=0, snap=False):
            '''Interactively change the current frame number
               Arguments:
               @frame (int): in [-500000, 500000], (optional)
               @snap (bool): (optional)

            '''

            pass

        def channel_select_keys(extend=False):
            '''Select all keyframes of channel under mouse
               Arguments:
               @extend (bool): Extend selection
                  (optional)

            '''

            pass

        def channels_clean_empty():
            '''Delete all empty animation data containers from visible datablocks
            '''

            pass

        def channels_click(extend=False, children_only=False):
            '''Handle mouse-clicks over animation channels
               Arguments:
               @extend (bool): (optional)
               @children_only (bool): (optional)

            '''

            pass

        def channels_collapse(all=True):
            '''Collapse (i.e. close) all selected expandable animation channels
               Arguments:
               @all (bool): Collapse all channels (not just selected ones)
                  (optional)

            '''

            pass

        def channels_delete():
            '''Delete all selected animation channels
            '''

            pass

        def channels_editable_toggle(mode='TOGGLE', type='PROTECT'):
            '''Toggle editability of selected channels
               Arguments:
               @mode (str): in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
               @type (str): in ['PROTECT', 'MUTE'], (optional)

            '''

            pass

        def channels_expand(all=True):
            '''Expand (i.e. open) all selected expandable animation channels
               Arguments:
               @all (bool): Expand all channels (not just selected ones)
                  (optional)

            '''

            pass

        def channels_fcurves_enable():
            '''Clears 'disabled' tag from all F-Curves to get broken F-Curves working again
            '''

            pass

        def channels_find(query="Query"):
            '''Filter the set of channels shown to only include those with matching names
               Arguments:
               @query (str): Text to search for in channel names
                  (optional, never None)

            '''

            pass

        def channels_group(name="New Group"):
            '''Add selected F-Curves to a new group
               Arguments:
               @name (str): Name of newly created group
                  (optional, never None)

            '''

            pass

        def channels_move(direction='DOWN'):
            '''Rearrange selected animation channels
               Arguments:
               @direction (str): in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional)

            '''

            pass

        def channels_rename():
            '''Rename animation channel under mouse
            '''

            pass

        def channels_select_all_toggle(invert=False):
            '''Toggle selection of all animation channels
               Arguments:
               @invert (bool): (optional)

            '''

            pass

        def channels_select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select all animation channels within the specified region
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def channels_setting_disable(mode='DISABLE', type='PROTECT'):
            '''Disable specified setting on all selected animation channels
               Arguments:
               @mode (str): in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
               @type (str): in ['PROTECT', 'MUTE'], (optional)

            '''

            pass

        def channels_setting_enable(mode='ENABLE', type='PROTECT'):
            '''Enable specified setting on all selected animation channels
               Arguments:
               @mode (str): in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
               @type (str): in ['PROTECT', 'MUTE'], (optional)

            '''

            pass

        def channels_setting_toggle(mode='TOGGLE', type='PROTECT'):
            '''Toggle specified setting on all selected animation channels
               Arguments:
               @mode (str): in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
               @type (str): in ['PROTECT', 'MUTE'], (optional)

            '''

            pass

        def channels_ungroup():
            '''Remove selected F-Curves from their current groups
            '''

            pass

        def clear_useless_actions(only_unused=True):
            '''Mark actions with no F-Curves for deletion after save & reload of file preserving "action libraries"
               Arguments:
               @only_unused (bool): Only unused (Fake User only) actions get considered
                  (optional)

            '''

            pass

        def copy_driver_button():
            '''Copy the driver for the highlighted button
            '''

            pass

        def driver_button_add(mapping_type='SINGLE_MANY'):
            '''Add driver(s) for the property(s) represented by the highlighted button
               Arguments:
               @mapping_type (str): Method used to match target and driven properties
                  in ['SINGLE_MANY', 'DIRECT', 'MATCH', 'NONE_ALL', 'NONE_SINGLE'], (optional)

            '''

            pass

        def driver_button_remove(all=True):
            '''Remove the driver(s) for the property(s) connected represented by the highlighted button
               Arguments:
               @all (bool): Delete drivers for all elements of the array
                  (optional)

            '''

            pass

        def keyframe_clear_button(all=True):
            '''Clear all keyframes on the currently active property
               Arguments:
               @all (bool): Clear keyframes from all elements of the array
                  (optional)

            '''

            pass

        def keyframe_clear_v3d():
            '''Remove all keyframe animation for selected objects
            '''

            pass

        def keyframe_delete(type='DEFAULT', confirm_success=True):
            '''Delete keyframes on the current frame for all properties in the specified Keying Set
               Arguments:
               @type (str): The Keying Set to use
                  in ['DEFAULT'], (optional)
               @confirm_success (bool): Show a popup when the keyframes get successfully removed
                  (optional)

            '''

            pass

        def keyframe_delete_button(all=True):
            '''Delete current keyframe of current UI-active property
               Arguments:
               @all (bool): Delete keyframes from all elements of the array
                  (optional)

            '''

            pass

        def keyframe_delete_v3d():
            '''Remove keyframes on current frame for selected objects and bones
            '''

            pass

        def keyframe_insert(type='DEFAULT', confirm_success=True):
            '''Insert keyframes on the current frame for all properties in the specified Keying Set
               Arguments:
               @type (str): The Keying Set to use
                  in ['DEFAULT'], (optional)
               @confirm_success (bool): Show a popup when the keyframes get successfully added
                  (optional)

            '''

            pass

        def keyframe_insert_button(all=True):
            '''Insert a keyframe for current UI-active property
               Arguments:
               @all (bool): Insert a keyframe for all element of the array
                  (optional)

            '''

            pass

        def keyframe_insert_menu(type='DEFAULT', confirm_success=False, always_prompt=False):
            '''Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined
               Arguments:
               @type (str): The Keying Set to use
                  in ['DEFAULT'], (optional)
               @confirm_success (bool): Show a popup when the keyframes get successfully added
                  (optional)
               @always_prompt (bool): (optional)

            '''

            pass

        def keying_set_active_set(type='DEFAULT'):
            '''Select a new keying set as the active one
               Arguments:
               @type (str): The Keying Set to use
                  in ['DEFAULT'], (optional)

            '''

            pass

        def keying_set_add():
            '''Add a new (empty) Keying Set to the active Scene
            '''

            pass

        def keying_set_export(filepath="", filter_folder=True, filter_text=True, filter_python=True):
            '''Export Keying Set to a python script
               Arguments:
               @filepath (str): (optional, never None)
               @filter_folder (bool): (optional)
               @filter_text (bool): (optional)
               @filter_python (bool): (optional)

            '''

            pass

        def keying_set_path_add():
            '''Add empty path to active Keying Set
            '''

            pass

        def keying_set_path_remove():
            '''Remove active Path from active Keying Set
            '''

            pass

        def keying_set_remove():
            '''Remove the active Keying Set
            '''

            pass

        def keyingset_button_add(all=True):
            '''Add current UI-active property to current keying set
               Arguments:
               @all (bool): Add all elements of the array to a Keying Set
                  (optional)

            '''

            pass

        def keyingset_button_remove():
            '''Remove current UI-active property from current keying set
            '''

            pass

        def paste_driver_button():
            '''Paste the driver in the copy/paste buffer for the highlighted button
            '''

            pass

        def previewrange_clear():
            '''Clear Preview Range
            '''

            pass

        def previewrange_set(xmin=0, xmax=0, ymin=0, ymax=0):
            '''Interactively define frame range used for playback
               Arguments:
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def update_animated_transform_constraints(use_convert_to_radians=True):
            '''Update fcurves/drivers affecting Transform constraints (use it with files from 2.70 and earlier)
               Arguments:
               @use_convert_to_radians (bool): Convert fcurves/drivers affecting rotations to radians (Warning: use this only once!)
                  (optional)

            '''

            pass

    class armature:
        '''Spcecial class, created just to reflect content of bpy.ops.armature'''

        def align():
            '''Align selected bones to the active bone (or to their parent)
            '''

            pass

        def armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Change the visible armature layers
               Arguments:
               @layers (bool): Armature layers to make visible
                  array of 32 items, (optional)

            '''

            pass

        def autoside_names(type='XAXIS'):
            '''Automatically renames the selected bones according to which side of the target axis they fall on
               Arguments:
               @type (str): Axis tag names with
                  in ['XAXIS', 'YAXIS', 'ZAXIS'], (optional)

            '''

            pass

        def bone_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Change the layers that the selected bones belong to
               Arguments:
               @layers (bool): Armature layers that bone belongs to
                  array of 32 items, (optional)

            '''

            pass

        def bone_primitive_add(name="Bone"):
            '''Add a new bone located at the 3D-Cursor
               Arguments:
               @name (str): Name of the newly created bone
                  (optional, never None)

            '''

            pass

        def calculate_roll(type='POS_X', axis_flip=False, axis_only=False):
            '''Automatically fix alignment of select bones' axes
               Arguments:
               @type (str): in ['POS_X', 'POS_Z', 'GLOBAL_POS_X', 'GLOBAL_POS_Y', 'GLOBAL_POS_Z', 'NEG_X', 'NEG_Z', 'GLOBAL_NEG_X', 'GLOBAL_NEG_Y', 'GLOBAL_NEG_Z', 'ACTIVE', 'VIEW', 'CURSOR'], (optional)
               @axis_flip (bool): Negate the alignment axis
                  (optional)
               @axis_only (bool): Ignore the axis direction, use the shortest rotation to align
                  (optional)

            '''

            pass

        def click_extrude():
            '''Create a new bone going from the last selected joint to the mouse position
            '''

            pass

        def delete():
            '''Remove selected bones from the armature
            '''

            pass

        def dissolve():
            '''Dissolve selected bones from the armature
            '''

            pass

        def duplicate():
            '''Make copies of the selected bones within the same armature
            '''

            pass

        def duplicate_move(ARMATURE_OT_duplicate=None, TRANSFORM_OT_translate=None):
            '''Make copies of the selected bones within the same armature and move them
               Arguments:
               @ARMATURE_OT_duplicate (ARMATURE_OT_duplicate): Make copies of the selected bones within the same armature
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def extrude(forked=False):
            '''Create new bones from the selected joints
               Arguments:
               @forked (bool): (optional)

            '''

            pass

        def extrude_forked(ARMATURE_OT_extrude=None, TRANSFORM_OT_translate=None):
            '''Create new bones from the selected joints and move them
               Arguments:
               @ARMATURE_OT_extrude (ARMATURE_OT_extrude): Create new bones from the selected joints
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def extrude_move(ARMATURE_OT_extrude=None, TRANSFORM_OT_translate=None):
            '''Create new bones from the selected joints and move them
               Arguments:
               @ARMATURE_OT_extrude (ARMATURE_OT_extrude): Create new bones from the selected joints
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def fill():
            '''Add bone between selected joint(s) and/or 3D-Cursor
            '''

            pass

        def flip_names():
            '''Flips (and corrects) the axis suffixes of the names of selected bones
            '''

            pass

        def hide(unselected=False):
            '''Tag selected bones to not be visible in Edit Mode
               Arguments:
               @unselected (bool): Hide unselected rather than selected
                  (optional)

            '''

            pass

        def layers_show_all(all=True):
            '''Make all armature layers visible
               Arguments:
               @all (bool): Enable all layers or just the first 16 (top row)
                  (optional)

            '''

            pass

        def merge(type='WITHIN_CHAIN'):
            '''Merge continuous chains of selected bones
               Arguments:
               @type (str): in ['WITHIN_CHAIN'], (optional)

            '''

            pass

        def parent_clear(type='CLEAR'):
            '''Remove the parent-child relationship between selected bones and their parents
               Arguments:
               @type (str): What way to clear parenting
                  in ['CLEAR', 'DISCONNECT'], (optional)

            '''

            pass

        def parent_set(type='CONNECTED'):
            '''Set the active bone as the parent of the selected bones
               Arguments:
               @type (str): Type of parenting
                  in ['CONNECTED', 'OFFSET'], (optional)

            '''

            pass

        def reveal():
            '''Unhide all bones that have been tagged to be hidden in Edit Mode
            '''

            pass

        def roll_clear(roll=0.0):
            '''Clear roll for selected bones
               Arguments:
               @roll (float): in [-6.28319, 6.28319], (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''Toggle selection status of all bones
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_hierarchy(direction='PARENT', extend=False):
            '''Select immediate parent/children of selected bones
               Arguments:
               @direction (str): in ['PARENT', 'CHILD'], (optional)
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_less():
            '''Deselect those bones at the boundary of each selection region
            '''

            pass

        def select_linked(extend=False):
            '''Select bones related to selected ones by parent/child relationships
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_mirror(only_active=False, extend=False):
            '''Mirror the bone selection
               Arguments:
               @only_active (bool): Only operate on the active bone
                  (optional)
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_more():
            '''Select those bones connected to the initial selection
            '''

            pass

        def select_similar(type='LENGTH', threshold=0.1):
            '''Select similar bones by property types
               Arguments:
               @type (str): in ['CHILDREN', 'CHILDREN_IMMEDIATE', 'SIBLINGS', 'LENGTH', 'DIRECTION', 'PREFIX', 'SUFFIX', 'LAYER'], (optional)
               @threshold (float): in [0, 1], (optional)

            '''

            pass

        def separate():
            '''Isolate selected bones into a separate armature
            '''

            pass

        def shortest_path_pick():
            '''Select shortest path between two bones
            '''

            pass

        def split():
            '''Split off selected bones from connected unselected bones
            '''

            pass

        def subdivide(number_cuts=1):
            '''Break selected bones into chains of smaller bones
               Arguments:
               @number_cuts (int): in [1, 1000], (optional)

            '''

            pass

        def switch_direction():
            '''Change the direction that a chain of bones points in (head <-> tail swap)
            '''

            pass

        def symmetrize(direction='NEGATIVE_X'):
            '''Enforce symmetry, make copies of the selection or use existing
               Arguments:
               @direction (str): Which sides to copy from and to (when both are selected)
                  in ['NEGATIVE_X', 'POSITIVE_X'], (optional)

            '''

            pass

    class boid:
        '''Spcecial class, created just to reflect content of bpy.ops.boid'''

        def rule_add(type='GOAL'):
            '''Add a boid rule to the current boid state
               Arguments:
               @type (str): in ['GOAL', 'AVOID', 'AVOID_COLLISION', 'SEPARATE', 'FLOCK', 'FOLLOW_LEADER', 'AVERAGE_SPEED', 'FIGHT'], (optional)

            '''

            pass

        def rule_del():
            '''Delete current boid rule
            '''

            pass

        def rule_move_down():
            '''Move boid rule down in the list
            '''

            pass

        def rule_move_up():
            '''Move boid rule up in the list
            '''

            pass

        def state_add():
            '''Add a boid state to the particle system
            '''

            pass

        def state_del():
            '''Delete current boid state
            '''

            pass

        def state_move_down():
            '''Move boid state down in the list
            '''

            pass

        def state_move_up():
            '''Move boid state up in the list
            '''

            pass

    class brush:
        '''Spcecial class, created just to reflect content of bpy.ops.brush'''

        def active_index_set(mode="", index=0):
            '''Set active sculpt/paint brush from it's number
               Arguments:
               @mode (str): Paint mode to set brush for
                  (optional, never None)
               @index (int): Brush number
                  in [-inf, inf], (optional)

            '''

            pass

        def add():
            '''Add brush by mode type
            '''

            pass

        def curve_preset(shape='SMOOTH'):
            '''Set brush shape
               Arguments:
               @shape (str): in ['SHARP', 'SMOOTH', 'MAX', 'LINE', 'ROUND', 'ROOT'], (optional)

            '''

            pass

        def reset():
            '''Return brush to defaults based on current tool
            '''

            pass

        def scale_size(scalar=1.0):
            '''Change brush size by a scalar
               Arguments:
               @scalar (float): Factor to scale brush size by
                  in [0, 2], (optional)

            '''

            pass

        def stencil_control(mode='TRANSLATION', texmode='PRIMARY'):
            '''Control the stencil brush
               Arguments:
               @mode (str): in ['TRANSLATION', 'SCALE', 'ROTATION'], (optional)
               @texmode (str): in ['PRIMARY', 'SECONDARY'], (optional)

            '''

            pass

        def stencil_fit_image_aspect(use_repeat=True, use_scale=True, mask=False):
            '''When using an image texture, adjust the stencil size to fit the image aspect ratio
               Arguments:
               @use_repeat (bool): Use repeat mapping values
                  (optional)
               @use_scale (bool): Use texture scale values
                  (optional)
               @mask (bool): Modify either the primary or mask stencil
                  (optional)

            '''

            pass

        def stencil_reset_transform(mask=False):
            '''Reset the stencil transformation to the default
               Arguments:
               @mask (bool): Modify either the primary or mask stencil
                  (optional)

            '''

            pass

        def uv_sculpt_tool_set(tool='PINCH'):
            '''Set the UV sculpt tool
               Arguments:
               @tool (str): in ['PINCH', 'RELAX', 'GRAB'], (optional)

            '''

            pass

    class buttons:
        '''Spcecial class, created just to reflect content of bpy.ops.buttons'''

        def directory_browse(directory="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=False, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Open a directory browser, Hold Shift to open the file, Alt to browse containing directory
               Arguments:
               @directory (str): Directory of the file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def file_browse(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=False, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Open a file browser, Hold Shift to open the file, Alt to browse containing directory
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def toolbox():
            '''Display button panel toolbox
            '''

            pass

    class cachefile:
        '''Spcecial class, created just to reflect content of bpy.ops.cachefile'''

        def open(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Load a cache file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def reload():
            '''Update objects paths list with new data from the archive
            '''

            pass

    class camera:
        '''Spcecial class, created just to reflect content of bpy.ops.camera'''

        def preset_add(name="", remove_active=False, use_focal_length=False):
            '''Add or remove a Camera Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)
               @use_focal_length (bool): Include focal length into the preset
                  (optional)

            '''

            pass

    class clip:
        '''Spcecial class, created just to reflect content of bpy.ops.clip'''

        def add_marker(location=(0.0, 0.0)):
            '''Place new marker at specified location
               Arguments:
               @location (float): Location of marker on frame
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def add_marker_at_click():
            '''Place new marker at the desired (clicked) position
            '''

            pass

        def add_marker_move(CLIP_OT_add_marker=None, TRANSFORM_OT_translate=None):
            '''Add new marker and move it on movie
               Arguments:
               @CLIP_OT_add_marker (CLIP_OT_add_marker): Place new marker at specified location
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def add_marker_slide(CLIP_OT_add_marker=None, TRANSFORM_OT_translate=None):
            '''Add new marker and slide it with mouse until mouse button release
               Arguments:
               @CLIP_OT_add_marker (CLIP_OT_add_marker): Place new marker at specified location
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def apply_solution_scale(distance=0.0):
            '''Apply scale on solution itself to make distance between selected tracks equals to desired
               Arguments:
               @distance (float): Distance between selected tracks
                  in [-inf, inf], (optional)

            '''

            pass

        def bundles_to_mesh():
            '''Create vertex cloud using coordinates of reconstructed tracks
            '''

            pass

        def camera_preset_add(name="", remove_active=False, use_focal_length=True):
            '''Add or remove a Tracking Camera Intrinsics Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)
               @use_focal_length (bool): Include focal length into the preset
                  (optional)

            '''

            pass

        def change_frame(frame=0):
            '''Interactively change the current frame number
               Arguments:
               @frame (int): in [-500000, 500000], (optional)

            '''

            pass

        def clean_tracks(frames=0, error=0.0, action='SELECT'):
            '''Clean tracks with high error values or few frames
               Arguments:
               @frames (int): Effect on tracks which are tracked less than specified amount of frames
                  in [0, inf], (optional)
               @error (float): Effect on tracks which have got larger re-projection error
                  in [0, inf], (optional)
               @action (str): Cleanup action to execute
                  in ['SELECT', 'DELETE_TRACK', 'DELETE_SEGMENTS'], (optional)

            '''

            pass

        def clear_solution():
            '''Clear all calculated data
            '''

            pass

        def clear_track_path(action='REMAINED', clear_active=False):
            '''Clear tracks after/before current position or clear the whole track
               Arguments:
               @action (str): Clear action to execute
                  in ['UPTO', 'REMAINED', 'ALL'], (optional)
               @clear_active (bool): Clear active track only instead of all selected tracks
                  (optional)

            '''

            pass

        def constraint_to_fcurve():
            '''Create F-Curves for object which will copy object's movement caused by this constraint
            '''

            pass

        def copy_tracks():
            '''Copy selected tracks to clipboard
            '''

            pass

        def create_plane_track():
            '''Create new plane track out of selected point tracks
            '''

            pass

        def cursor_set(location=(0.0, 0.0)):
            '''Set 2D cursor location
               Arguments:
               @location (float): Cursor location in normalized clip coordinates
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def delete_marker():
            '''Delete marker for current frame from selected tracks
            '''

            pass

        def delete_proxy():
            '''Delete movie clip proxy files from the hard drive
            '''

            pass

        def delete_track():
            '''Delete selected tracks
            '''

            pass

        def detect_features(placement='FRAME', margin=16, threshold=0.5, min_distance=120):
            '''Automatically detect features and place markers to track
               Arguments:
               @placement (str): Placement for detected features
                  in ['FRAME', 'INSIDE_GPENCIL', 'OUTSIDE_GPENCIL'], (optional)
               @margin (int): Only features further than margin pixels from the image edges are considered
                  in [0, inf], (optional)
               @threshold (float): Threshold level to consider feature good enough for tracking
                  in [0.0001, inf], (optional)
               @min_distance (int): Minimal distance accepted between two features
                  in [0, inf], (optional)

            '''

            pass

        def disable_markers(action='DISABLE'):
            '''Disable/enable selected markers
               Arguments:
               @action (str): Disable action to execute
                  in ['DISABLE', 'ENABLE', 'TOGGLE'], (optional)

            '''

            pass

        def dopesheet_select_channel(location=(0.0, 0.0), extend=False):
            '''Select movie tracking channel
               Arguments:
               @location (float): Mouse location to select channel
                  array of 2 items in [-inf, inf], (optional)
               @extend (bool): Extend selection rather than clearing the existing selection
                  (optional)

            '''

            pass

        def dopesheet_view_all():
            '''Reset viewable area to show full keyframe range
            '''

            pass

        def filter_tracks(track_threshold=5.0):
            '''Filter tracks which has weirdly looking spikes in motion curves
               Arguments:
               @track_threshold (float): Filter Threshold to select problematic tracks
                  in [-inf, inf], (optional)

            '''

            pass

        def frame_jump(position='PATHSTART'):
            '''Jump to special frame
               Arguments:
               @position (str): Position to jump to
                  in ['PATHSTART', 'PATHEND', 'FAILEDPREV', 'FAILNEXT'], (optional)

            '''

            pass

        def graph_center_current_frame():
            '''Scroll view so current frame would be centered
            '''

            pass

        def graph_delete_curve():
            '''Delete track corresponding to the selected curve
            '''

            pass

        def graph_delete_knot():
            '''Delete curve knots
            '''

            pass

        def graph_disable_markers(action='DISABLE'):
            '''Disable/enable selected markers
               Arguments:
               @action (str): Disable action to execute
                  in ['DISABLE', 'ENABLE', 'TOGGLE'], (optional)

            '''

            pass

        def graph_select(location=(0.0, 0.0), extend=False):
            '''Select graph curves
               Arguments:
               @location (float): Mouse location to select nearest entity
                  array of 2 items in [-inf, inf], (optional)
               @extend (bool): Extend selection rather than clearing the existing selection
                  (optional)

            '''

            pass

        def graph_select_all_markers(action='TOGGLE'):
            '''Change selection of all markers of active track
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def graph_select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select curve points using border selection
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def graph_view_all():
            '''View all curves in editor
            '''

            pass

        def hide_tracks(unselected=False):
            '''Hide selected tracks
               Arguments:
               @unselected (bool): Hide unselected tracks
                  (optional)

            '''

            pass

        def hide_tracks_clear():
            '''Clear hide selected tracks
            '''

            pass

        def join_tracks():
            '''Join selected tracks
            '''

            pass

        def keyframe_delete():
            '''Delete a keyframe from selected tracks at current frame
            '''

            pass

        def keyframe_insert():
            '''Insert a keyframe to selected tracks at current frame
            '''

            pass

        def lock_tracks(action='LOCK'):
            '''Lock/unlock selected tracks
               Arguments:
               @action (str): Lock action to execute
                  in ['LOCK', 'UNLOCK', 'TOGGLE'], (optional)

            '''

            pass

        def mode_set(mode='TRACKING'):
            '''Set the clip interaction mode
               Arguments:
               @mode (str): in ['TRACKING', 'MASK'], (optional)

            '''

            pass

        def open(directory="", files=None, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Load a sequence of frames or a movie file
               Arguments:
               @directory (str): Directory of the file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def paste_tracks():
            '''Paste tracks from clipboard
            '''

            pass

        def prefetch():
            '''Prefetch frames from disk for faster playback/tracking
            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def rebuild_proxy():
            '''Rebuild all selected proxies and timecode indices in the background
            '''

            pass

        def refine_markers(backwards=False):
            '''Refine selected markers positions by running the tracker from track's reference to current frame
               Arguments:
               @backwards (bool): Do backwards tracking
                  (optional)

            '''

            pass

        def reload():
            '''Reload clip
            '''

            pass

        def select(extend=False, location=(0.0, 0.0)):
            '''Select tracking markers
               Arguments:
               @extend (bool): Extend selection rather than clearing the existing selection
                  (optional)
               @location (float): Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''Change selection of all tracking markers
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select markers using border selection
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_circle(x=0, y=0, radius=1, gesture_mode=0):
            '''Select markers using circle selection
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @radius (int): in [1, inf], (optional)
               @gesture_mode (int): in [-inf, inf], (optional)

            '''

            pass

        def select_grouped(group='ESTIMATED'):
            '''Select all tracks from specified group
               Arguments:
               @group (str): Clear action to execute
                  in ['KEYFRAMED', 'ESTIMATED', 'TRACKED', 'LOCKED', 'DISABLED', 'COLOR', 'FAILED'], (optional)

            '''

            pass

        def select_lasso(path=None, deselect=False, extend=True):
            '''Select markers using lasso selection
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @deselect (bool): Deselect rather than select items
                  (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def set_active_clip():
            '''undocumented
            '''

            pass

        def set_axis(axis='X'):
            '''Set direction of scene axis rotating camera (or its parent if present) and assume selected track lies on real axis, joining it with the origin
               Arguments:
               @axis (str): Axis to use to align bundle along
                  in ['X', 'Y'], (optional)

            '''

            pass

        def set_center_principal():
            '''Set optical center to center of footage
            '''

            pass

        def set_origin(use_median=False):
            '''Set active marker as origin by moving camera (or its parent if present) in 3D space
               Arguments:
               @use_median (bool): Set origin to median point of selected bundles
                  (optional)

            '''

            pass

        def set_plane(plane='FLOOR'):
            '''Set plane based on 3 selected bundles by moving camera (or its parent if present) in 3D space
               Arguments:
               @plane (str): Plane to be used for orientation
                  in ['FLOOR', 'WALL'], (optional)

            '''

            pass

        def set_scale(distance=0.0):
            '''Set scale of scene by scaling camera (or its parent if present)
               Arguments:
               @distance (float): Distance between selected tracks
                  in [-inf, inf], (optional)

            '''

            pass

        def set_scene_frames():
            '''Set scene's start and end frame to match clip's start frame and length
            '''

            pass

        def set_solution_scale(distance=0.0):
            '''Set object solution scale using distance between two selected tracks
               Arguments:
               @distance (float): Distance between selected tracks
                  in [-inf, inf], (optional)

            '''

            pass

        def set_solver_keyframe(keyframe='KEYFRAME_A'):
            '''Set keyframe used by solver
               Arguments:
               @keyframe (str): Keyframe to set
                  in ['KEYFRAME_A', 'KEYFRAME_B'], (optional)

            '''

            pass

        def set_viewport_background():
            '''Set current movie clip as a camera background in 3D view-port (works only when a 3D view-port is visible)
            '''

            pass

        def setup_tracking_scene():
            '''Prepare scene for compositing 3D objects into this footage
            '''

            pass

        def slide_marker(offset=(0.0, 0.0)):
            '''Slide marker areas
               Arguments:
               @offset (float): Offset in floating point units, 1.0 is the width and height of the image
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def slide_plane_marker():
            '''Slide plane marker areas
            '''

            pass

        def solve_camera():
            '''Solve camera motion from tracks
            '''

            pass

        def stabilize_2d_add():
            '''Add selected tracks to 2D translation stabilization
            '''

            pass

        def stabilize_2d_remove():
            '''Remove selected track from translation stabilization
            '''

            pass

        def stabilize_2d_rotation_add():
            '''Add selected tracks to 2D rotation stabilization
            '''

            pass

        def stabilize_2d_rotation_remove():
            '''Remove selected track from rotation stabilization
            '''

            pass

        def stabilize_2d_rotation_select():
            '''Select tracks which are used for rotation stabilization
            '''

            pass

        def stabilize_2d_select():
            '''Select tracks which are used for translation stabilization
            '''

            pass

        def tools():
            '''Toggle clip tools panel
            '''

            pass

        def track_color_preset_add(name="", remove_active=False):
            '''Add or remove a Clip Track Color Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def track_copy_color():
            '''Copy color to all selected tracks
            '''

            pass

        def track_markers(backwards=False, sequence=False):
            '''Track selected markers
               Arguments:
               @backwards (bool): Do backwards tracking
                  (optional)
               @sequence (bool): Track marker during image sequence rather than single image
                  (optional)

            '''

            pass

        def track_settings_as_default():
            '''Copy tracking settings from active track to default settings
            '''

            pass

        def track_settings_to_track():
            '''Copy tracking settings from active track to selected tracks
            '''

            pass

        def track_to_empty():
            '''Create an Empty object which will be copying movement of active track
            '''

            pass

        def tracking_object_new():
            '''Add new object for tracking
            '''

            pass

        def tracking_object_remove():
            '''Remove object for tracking
            '''

            pass

        def tracking_settings_preset_add(name="", remove_active=False):
            '''Add or remove a motion tracking settings preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def view_all(fit_view=False):
            '''View whole image with markers
               Arguments:
               @fit_view (bool): Fit frame to the viewport
                  (optional)

            '''

            pass

        def view_ndof():
            '''Use a 3D mouse device to pan/zoom the view
            '''

            pass

        def view_pan(offset=(0.0, 0.0)):
            '''Pan the view
               Arguments:
               @offset (float): Offset in floating point units, 1.0 is the width and height of the image
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def view_selected():
            '''View all selected elements
            '''

            pass

        def view_zoom(factor=0.0):
            '''Zoom in/out the view
               Arguments:
               @factor (float): Zoom factor, values higher than 1.0 zoom in, lower values zoom out
                  in [-inf, inf], (optional)

            '''

            pass

        def view_zoom_in(location=(0.0, 0.0)):
            '''Zoom in the view
               Arguments:
               @location (float): Cursor location in screen coordinates
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def view_zoom_out(location=(0.0, 0.0)):
            '''Zoom out the view
               Arguments:
               @location (float): Cursor location in normalized (0.0-1.0) coordinates
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def view_zoom_ratio(ratio=0.0):
            '''Set the zoom ratio (based on clip size)
               Arguments:
               @ratio (float): Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
                  in [-inf, inf], (optional)

            '''

            pass

    class cloth:
        '''Spcecial class, created just to reflect content of bpy.ops.cloth'''

        def preset_add(name="", remove_active=False):
            '''Add or remove a Cloth Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

    class console:
        '''Spcecial class, created just to reflect content of bpy.ops.console'''

        def autocomplete():
            '''Evaluate the namespace up until the cursor and give a list of options or complete the name if there is only one
            '''

            pass

        def banner():
            '''Print a message when the terminal initializes
            '''

            pass

        def clear(scrollback=True, history=False):
            '''Clear text by type
               Arguments:
               @scrollback (bool): Clear the scrollback history
                  (optional)
               @history (bool): Clear the command history
                  (optional)

            '''

            pass

        def clear_line():
            '''Clear the line and store in history
            '''

            pass

        def copy():
            '''Copy selected text to clipboard
            '''

            pass

        def copy_as_script():
            '''Copy the console contents for use in a script
            '''

            pass

        def delete(type='NEXT_CHARACTER'):
            '''Delete text by cursor position
               Arguments:
               @type (str): Which part of the text to delete
                  in ['NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'NEXT_WORD', 'PREVIOUS_WORD'], (optional)

            '''

            pass

        def execute(interactive=False):
            '''Execute the current console line as a python expression
               Arguments:
               @interactive (bool): (optional)

            '''

            pass

        def history_append(text="", current_character=0, remove_duplicates=False):
            '''Append history at cursor position
               Arguments:
               @text (str): Text to insert at the cursor position
                  (optional, never None)
               @current_character (int): The index of the cursor
                  in [0, inf], (optional)
               @remove_duplicates (bool): Remove duplicate items in the history
                  (optional)

            '''

            pass

        def history_cycle(reverse=False):
            '''Cycle through history
               Arguments:
               @reverse (bool): Reverse cycle history
                  (optional)

            '''

            pass

        def indent():
            '''Add 4 spaces at line beginning
            '''

            pass

        def insert(text=""):
            '''Insert text at cursor position
               Arguments:
               @text (str): Text to insert at the cursor position
                  (optional, never None)

            '''

            pass

        def language(language=""):
            '''Set the current language for this console
               Arguments:
               @language (str): (optional, never None)

            '''

            pass

        def move(type='LINE_BEGIN'):
            '''Move cursor position
               Arguments:
               @type (str): Where to move cursor to
                  in ['LINE_BEGIN', 'LINE_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD'], (optional)

            '''

            pass

        def paste():
            '''Paste text from clipboard
            '''

            pass

        def scrollback_append(text="", type='OUTPUT'):
            '''Append scrollback text by type
               Arguments:
               @text (str): Text to insert at the cursor position
                  (optional, never None)
               @type (str): Console output type
                  in ['OUTPUT', 'INPUT', 'INFO', 'ERROR'], (optional)

            '''

            pass

        def select_set():
            '''Set the console selection
            '''

            pass

        def select_word():
            '''Select word at cursor position
            '''

            pass

        def unindent():
            '''Delete 4 spaces from line beginning
            '''

            pass

    class constraint:
        '''Spcecial class, created just to reflect content of bpy.ops.constraint'''

        def childof_clear_inverse(constraint="", owner='OBJECT'):
            '''Clear inverse correction for ChildOf constraint
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)

            '''

            pass

        def childof_set_inverse(constraint="", owner='OBJECT'):
            '''Set inverse correction for ChildOf constraint
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)

            '''

            pass

        def delete():
            '''Remove constraint from constraint stack
            '''

            pass

        def followpath_path_animate(constraint="", owner='OBJECT', frame_start=1, length=100):
            '''Add default animation for path used by constraint if it isn't animated already
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)
               @frame_start (int): First frame of path animation
                  in [-500000, 500000], (optional)
               @length (int): Number of frames that path animation should take
                  in [0, 500000], (optional)

            '''

            pass

        def limitdistance_reset(constraint="", owner='OBJECT'):
            '''Reset limiting distance for Limit Distance Constraint
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)

            '''

            pass

        def move_down(constraint="", owner='OBJECT'):
            '''Move constraint down in constraint stack
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)

            '''

            pass

        def move_up(constraint="", owner='OBJECT'):
            '''Move constraint up in constraint stack
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)

            '''

            pass

        def objectsolver_clear_inverse(constraint="", owner='OBJECT'):
            '''Clear inverse correction for ObjectSolver constraint
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)

            '''

            pass

        def objectsolver_set_inverse(constraint="", owner='OBJECT'):
            '''Set inverse correction for ObjectSolver constraint
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)

            '''

            pass

        def stretchto_reset(constraint="", owner='OBJECT'):
            '''Reset original length of bone for Stretch To Constraint
               Arguments:
               @constraint (str): Name of the constraint to edit
                  (optional, never None)
               @owner (str): The owner of this constraint
                  in ['OBJECT', 'BONE'], (optional)

            '''

            pass

    class curve:
        '''Spcecial class, created just to reflect content of bpy.ops.curve'''

        def cyclic_toggle(direction='CYCLIC_U'):
            '''Make active spline closed/opened loop
               Arguments:
               @direction (str): Direction to make surface cyclic in
                  in ['CYCLIC_U', 'CYCLIC_V'], (optional)

            '''

            pass

        def de_select_first():
            '''(De)select first of visible part of each NURBS
            '''

            pass

        def de_select_last():
            '''(De)select last of visible part of each NURBS
            '''

            pass

        def delete(type='VERT'):
            '''Delete selected control points or segments
               Arguments:
               @type (str): Which elements to delete
                  in ['VERT', 'SEGMENT'], (optional)

            '''

            pass

        def dissolve_verts():
            '''Delete selected control points, correcting surrounding handles
            '''

            pass

        def draw(error_threshold=0.0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=None, wait_for_input=True):
            '''Draw a freehand spline
               Arguments:
               @error_threshold (float): Error distance threshold (in object units)
                  in [0, 10], (optional)
               @fit_method (str): in ['REFIT', 'SPLIT'], (optional)
               @corner_angle (float): in [0, 3.14159], (optional)
               @use_cyclic (bool): (optional)
               @stroke (OperatorStrokeElement): Collection of , (optional)
               @wait_for_input (bool): (optional)

            '''

            pass

        def duplicate():
            '''Duplicate selected control points
            '''

            pass

        def duplicate_move(CURVE_OT_duplicate=None, TRANSFORM_OT_translate=None):
            '''Duplicate curve and move
               Arguments:
               @CURVE_OT_duplicate (CURVE_OT_duplicate): Duplicate selected control points
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def extrude(mode='TRANSLATION'):
            '''Extrude selected control point(s)
               Arguments:
               @mode (str): in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)

            '''

            pass

        def extrude_move(CURVE_OT_extrude=None, TRANSFORM_OT_translate=None):
            '''Extrude curve and move result
               Arguments:
               @CURVE_OT_extrude (CURVE_OT_extrude): Extrude selected control point(s)
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def handle_type_set(type='AUTOMATIC'):
            '''Set type of handles for selected control points
               Arguments:
               @type (str): Spline type
                  in ['AUTOMATIC', 'VECTOR', 'ALIGNED', 'FREE_ALIGN', 'TOGGLE_FREE_ALIGN'], (optional)

            '''

            pass

        def hide(unselected=False):
            '''Hide (un)selected control points
               Arguments:
               @unselected (bool): Hide unselected rather than selected
                  (optional)

            '''

            pass

        def make_segment():
            '''Join two curves by their selected ends
            '''

            pass

        def match_texture_space():
            '''Match texture space to object's bounding box
            '''

            pass

        def normals_make_consistent(calc_length=False):
            '''Recalculate the direction of selected handles
               Arguments:
               @calc_length (bool): Recalculate handle length
                  (optional)

            '''

            pass

        def primitive_bezier_circle_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Bezier Circle
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_bezier_curve_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Bezier Curve
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_nurbs_circle_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Nurbs Circle
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_nurbs_curve_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Nurbs Curve
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_nurbs_path_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Path
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def radius_set(radius=1.0):
            '''Set per-point radius which is used for bevel tapering
               Arguments:
               @radius (float): in [0, inf], (optional)

            '''

            pass

        def reveal():
            '''Show again hidden control points
            '''

            pass

        def select_all(action='TOGGLE'):
            '''(De)select all control points
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_less():
            '''Reduce current selection by deselecting boundary elements
            '''

            pass

        def select_linked():
            '''Select all control points linked to active one
            '''

            pass

        def select_linked_pick(deselect=False):
            '''Select all control points linked to already selected ones
               Arguments:
               @deselect (bool): Deselect linked control points rather than selecting them
                  (optional)

            '''

            pass

        def select_more():
            '''Select control points directly linked to already selected ones
            '''

            pass

        def select_next():
            '''Select control points following already selected ones along the curves
            '''

            pass

        def select_nth(nth=2, skip=1, offset=0):
            '''Deselect every other vertex
               Arguments:
               @nth (int): in [2, inf], (optional)
               @skip (int): in [1, inf], (optional)
               @offset (int): in [-inf, inf], (optional)

            '''

            pass

        def select_previous():
            '''Select control points preceding already selected ones along the curves
            '''

            pass

        def select_random(percent=50.0, seed=0, action='SELECT'):
            '''Randomly select some control points
               Arguments:
               @percent (float): Percentage of objects to select randomly
                  in [0, 100], (optional)
               @seed (int): Seed for the random number generator
                  in [0, inf], (optional)
               @action (str): Selection action to execute
                  in ['SELECT', 'DESELECT'], (optional)

            '''

            pass

        def select_row():
            '''Select a row of control points including active one
            '''

            pass

        def select_similar(type='WEIGHT', compare='EQUAL', threshold=0.1):
            '''Select similar curve points by property type
               Arguments:
               @type (str): in ['TYPE', 'RADIUS', 'WEIGHT', 'DIRECTION'], (optional)
               @compare (str): in ['EQUAL', 'GREATER', 'LESS'], (optional)
               @threshold (float): in [0, inf], (optional)

            '''

            pass

        def separate():
            '''Separate selected points from connected unselected points into a new object
            '''

            pass

        def shade_flat():
            '''Set shading to flat
            '''

            pass

        def shade_smooth():
            '''Set shading to smooth
            '''

            pass

        def shortest_path_pick():
            '''Select shortest path between two selections
            '''

            pass

        def smooth():
            '''Flatten angles of selected points
            '''

            pass

        def smooth_radius():
            '''Interpolate radii of selected points
            '''

            pass

        def smooth_tilt():
            '''Interpolate tilt of selected points
            '''

            pass

        def smooth_weight():
            '''Interpolate weight of selected points
            '''

            pass

        def spin(center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
            '''Extrude selected boundary row around pivot point and current view axis
               Arguments:
               @center (float): Center in global view space
                  array of 3 items in [-inf, inf], (optional)
               @axis (float): Axis in global view space
                  array of 3 items in [-1, 1], (optional)

            '''

            pass

        def spline_type_set(type='POLY', use_handles=False):
            '''Set type of active spline
               Arguments:
               @type (str): Spline type
                  in ['POLY', 'BEZIER', 'NURBS'], (optional)
               @use_handles (bool): Use handles when converting bezier curves into polygons
                  (optional)

            '''

            pass

        def spline_weight_set(weight=1.0):
            '''Set softbody goal weight for selected points
               Arguments:
               @weight (float): in [0, 1], (optional)

            '''

            pass

        def split():
            '''Split off selected points from connected unselected points
            '''

            pass

        def subdivide(number_cuts=1):
            '''Subdivide selected segments
               Arguments:
               @number_cuts (int): in [1, 1000], (optional)

            '''

            pass

        def switch_direction():
            '''Switch direction of selected splines
            '''

            pass

        def tilt_clear():
            '''Clear the tilt of selected control points
            '''

            pass

        def vertex_add(location=(0.0, 0.0, 0.0)):
            '''Add a new control point (linked to only selected end-curve one, if any)
               Arguments:
               @location (float): Location to add new vertex at
                  array of 3 items in [-inf, inf], (optional)

            '''

            pass

    class cycles:
        '''Spcecial class, created just to reflect content of bpy.ops.cycles'''

        def use_shading_nodes():
            '''Enable nodes on a material, world or lamp
            '''

            pass

    class dpaint:
        '''Spcecial class, created just to reflect content of bpy.ops.dpaint'''

        def bake():
            '''Bake dynamic paint image sequence surface
            '''

            pass

        def output_toggle(output='A'):
            '''Add or remove Dynamic Paint output data layer
               Arguments:
               @output (str): in ['A', 'B'], (optional)

            '''

            pass

        def surface_slot_add():
            '''Add a new Dynamic Paint surface slot
            '''

            pass

        def surface_slot_remove():
            '''Remove the selected surface slot
            '''

            pass

        def type_toggle(type='CANVAS'):
            '''Toggle whether given type is active or not
               Arguments:
               @type (str): in ['CANVAS', 'BRUSH'], (optional)

            '''

            pass

    class ed:
        '''Spcecial class, created just to reflect content of bpy.ops.ed'''

        def flush_edits():
            '''Flush edit data from active editing modes
            '''

            pass

        def redo():
            '''Redo previous action
            '''

            pass

        def undo():
            '''Undo previous action
            '''

            pass

        def undo_history(item=0):
            '''Redo specific action in history
               Arguments:
               @item (int): in [0, inf], (optional)

            '''

            pass

        def undo_push(message="Add an undo step *function may be moved*"):
            '''Add an undo state (internal use only)
               Arguments:
               @message (str): (optional, never None)

            '''

            pass

    class export_anim:
        '''Spcecial class, created just to reflect content of bpy.ops.export_anim'''

        def bvh(filepath="", check_existing=True, filter_glob="*.bvh", global_scale=1.0, frame_start=0, frame_end=0, rotate_mode='NATIVE', root_transform_only=False):
            '''Save a BVH motion capture file from an armature
               Arguments:
               @filepath (str): Filepath used for exporting the file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_glob (str): (optional, never None)
               @global_scale (float): Scale the BVH by this value
                  in [0.0001, 1e+06], (optional)
               @frame_start (int): Starting frame to export
                  in [-inf, inf], (optional)
               @frame_end (int): End frame to export
                  in [-inf, inf], (optional)
               @rotate_mode (str): Rotation conversion
                  in ['NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'], (optional)
               @root_transform_only (bool): Only write out translation channels for the root bone
                  (optional)

            '''

            pass

    class export_mesh:
        '''Spcecial class, created just to reflect content of bpy.ops.export_mesh'''

        def ply(filepath="", check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.ply", use_mesh_modifiers=True, use_normals=True, use_uv_coords=True, use_colors=True, global_scale=1.0):
            '''Export a single object as a Stanford PLY with normals, colors and texture coordinates
               Arguments:
               @filepath (str): Filepath used for exporting the file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @use_mesh_modifiers (bool): Apply Modifiers to the exported mesh
                  (optional)
               @use_normals (bool): Export Normals for smooth and hard shaded faces (hard shaded faces will be exported as individual faces)
                  (optional)
               @use_uv_coords (bool): Export the active UV layer
                  (optional)
               @use_colors (bool): Export the active vertex color layer
                  (optional)
               @global_scale (float): in [0.01, 1000], (optional)

            '''

            pass

        def stl(filepath="", check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.stl", use_selection=False, global_scale=1.0, use_scene_unit=False, ascii=False, use_mesh_modifiers=True, batch_mode='OFF'):
            '''Save STL triangle mesh data from the active object
               Arguments:
               @filepath (str): Filepath used for exporting the file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @use_selection (bool): Export selected objects only
                  (optional)
               @global_scale (float): in [0.01, 1000], (optional)
               @use_scene_unit (bool): Apply current scene's unit (as defined by unit scale) to exported data
                  (optional)
               @ascii (bool): Save the file in ASCII file format
                  (optional)
               @use_mesh_modifiers (bool): Apply the modifiers before saving
                  (optional)
               @batch_mode (str): in ['OFF', 'OBJECT'], (optional)

            '''

            pass

    class export_scene:
        '''Spcecial class, created just to reflect content of bpy.ops.export_scene'''

        def autodesk_3ds(filepath="", check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.3ds", use_selection=False):
            '''Export to 3DS file format (.3ds)
               Arguments:
               @filepath (str): Filepath used for exporting the file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @use_selection (bool): Export selected objects only
                  (optional)

            '''

            pass

        def fbx(filepath="", check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx", version='BIN7400', ui_tab='MAIN', use_selection=False, global_scale=1.0, apply_unit_scale=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LAMP', 'MESH', 'OTHER'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, use_anim=True, use_anim_action_all=True, use_default_take=True, use_anim_optimize=True, anim_optimize_precision=6.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True):
            '''Write a FBX file
               Arguments:
               @filepath (str): Filepath used for exporting the file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @version (str): Choose which version of the exporter to use
                  in ['BIN7400', 'ASCII6100'], (optional)
               @ui_tab (str): Export options categories
                  in ['MAIN', 'GEOMETRY', 'ARMATURE', 'ANIMATION'], (optional)
               @use_selection (bool): Export selected objects on visible layers
                  (optional)
               @global_scale (float): Scale all data (Some importers do not support scaled armatures!)
                  in [0.001, 1000], (optional)
               @apply_unit_scale (bool): Scale all data according to current Blender size, to match default FBX unit (centimeter, some importers do not handle UnitScaleFactor properly)
                  (optional)
               @bake_space_transform (bool): Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
                  (optional)
               @object_types (str): Which kind of object to export
                  set in {'EMPTY', 'CAMERA', 'LAMP', 'ARMATURE', 'MESH', 'OTHER'}, (optional)
               @use_mesh_modifiers (bool): Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys
                  (optional)
               @mesh_smooth_type (str): Export smoothing information (prefer 'Normals Only' option if your target importer understand split normals)
                  in ['OFF', 'FACE', 'EDGE'], (optional)
               @use_mesh_edges (bool): Export loose edges (as two-vertices polygons)
                  (optional)
               @use_tspace (bool): Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)
                  (optional)
               @use_custom_props (bool): Export custom properties
                  (optional)
               @add_leaf_bones (bool): Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)
                  (optional)
               @primary_bone_axis (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @secondary_bone_axis (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @use_armature_deform_only (bool): Only write deforming bones (and non-deforming ones when they have deforming children)
                  (optional)
               @armature_nodetype (str): FBX type of node (object) used to represent Blender's armatures (use Null one unless you experience issues with other app, other choices may no import back perfectly in Blender...)
                  in ['NULL', 'ROOT', 'LIMBNODE'], (optional)
               @bake_anim (bool): Export baked keyframe animation
                  (optional)
               @bake_anim_use_all_bones (bool): Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)
                  (optional)
               @bake_anim_use_nla_strips (bool): Export each non-muted NLA strip as a separated FBX's AnimStack, if any, instead of global scene animation
                  (optional)
               @bake_anim_use_all_actions (bool): Export each action as a separated FBX's AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)
                  (optional)
               @bake_anim_force_startend_keying (bool): Always add a keyframe at start and end of actions for animated channels
                  (optional)
               @bake_anim_step (float): How often to evaluate animated values (in frames)
                  in [0.01, 100], (optional)
               @bake_anim_simplify_factor (float): How much to simplify baked values (0.0 to disable, the higher the more simplified)
                  in [0, 100], (optional)
               @use_anim (bool): Export keyframe animation
                  (optional)
               @use_anim_action_all (bool): Export all actions for armatures or just the currently selected action
                  (optional)
               @use_default_take (bool): Export currently assigned object and armature animations into a default take from the scene start/end frames
                  (optional)
               @use_anim_optimize (bool): Remove double keyframes
                  (optional)
               @anim_optimize_precision (float): Tolerance for comparing double keyframes (higher for greater accuracy)
                  in [0, 20], (optional)
               @path_mode (str): Method used to reference paths
                  in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY'], (optional)
               @embed_textures (bool): Embed textures in FBX binary file (only for "Copy" path mode!)
                  (optional)
               @batch_mode (str): in ['OFF', 'SCENE', 'GROUP'], (optional)
               @use_batch_own_dir (bool): Create a dir for each exported file
                  (optional)
               @use_metadata (bool): (optional)

            '''

            pass

        def obj(filepath="", check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=False, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1.0, path_mode='AUTO'):
            '''Save a Wavefront OBJ File
               Arguments:
               @filepath (str): Filepath used for exporting the file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @use_selection (bool): Export selected objects only
                  (optional)
               @use_animation (bool): Write out an OBJ for each frame
                  (optional)
               @use_mesh_modifiers (bool): Apply modifiers (preview resolution)
                  (optional)
               @use_edges (bool): (optional)
               @use_smooth_groups (bool): Write sharp edges as smooth groups
                  (optional)
               @use_smooth_groups_bitflags (bool): Same as 'Smooth Groups', but generate smooth groups IDs as bitflags (produces at most 32 different smooth groups, usually much less)
                  (optional)
               @use_normals (bool): Export one normal per vertex and per face, to represent flat faces and sharp edges
                  (optional)
               @use_uvs (bool): Write out the active UV coordinates
                  (optional)
               @use_materials (bool): Write out the MTL file
                  (optional)
               @use_triangles (bool): Convert all faces to triangles
                  (optional)
               @use_nurbs (bool): Write nurbs curves as OBJ nurbs rather than converting to geometry
                  (optional)
               @use_vertex_groups (bool): (optional)
               @use_blen_objects (bool): (optional)
               @group_by_object (bool): (optional)
               @group_by_material (bool): (optional)
               @keep_vertex_order (bool): (optional)
               @global_scale (float): in [0.01, 1000], (optional)
               @path_mode (str): Method used to reference paths
                  in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY'], (optional)

            '''

            pass

        def x3d(filepath="", check_existing=True, axis_forward='Z', axis_up='Y', filter_glob="*.x3d", use_selection=False, use_mesh_modifiers=True, use_triangulate=False, use_normals=False, use_compress=False, use_hierarchy=True, name_decorations=True, use_h3d=False, global_scale=1.0, path_mode='AUTO'):
            '''Export selection to Extensible 3D file (.x3d)
               Arguments:
               @filepath (str): Filepath used for exporting the file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @use_selection (bool): Export selected objects only
                  (optional)
               @use_mesh_modifiers (bool): Use transformed mesh data from each object
                  (optional)
               @use_triangulate (bool): Write quads into 'IndexedTriangleSet'
                  (optional)
               @use_normals (bool): Write normals with geometry
                  (optional)
               @use_compress (bool): Compress the exported file
                  (optional)
               @use_hierarchy (bool): Export parent child relationships
                  (optional)
               @name_decorations (bool): Add prefixes to the names of exported nodes to indicate their type
                  (optional)
               @use_h3d (bool): Export shaders for H3D
                  (optional)
               @global_scale (float): in [0.01, 1000], (optional)
               @path_mode (str): Method used to reference paths
                  in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY'], (optional)

            '''

            pass

    class file:
        '''Spcecial class, created just to reflect content of bpy.ops.file'''

        def autopack_toggle():
            '''Automatically pack all external files into the .blend file
            '''

            pass

        def bookmark_add():
            '''Add a bookmark for the selected/active directory
            '''

            pass

        def bookmark_cleanup():
            '''Delete all invalid bookmarks
            '''

            pass

        def bookmark_delete(index=-1):
            '''Delete selected bookmark
               Arguments:
               @index (int): in [-1, 20000], (optional)

            '''

            pass

        def bookmark_move(direction='TOP'):
            '''Move the active bookmark up/down in the list
               Arguments:
               @direction (str): Direction to move, UP or DOWN
                  in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional)

            '''

            pass

        def bookmark_toggle():
            '''Toggle bookmarks display
            '''

            pass

        def cancel():
            '''Cancel loading of selected file
            '''

            pass

        def delete():
            '''Delete selected files
            '''

            pass

        def directory_new(directory="", open=False):
            '''Create a new directory
               Arguments:
               @directory (str): Name of new directory
                  (optional, never None)
               @open (bool): Open new directory
                  (optional)

            '''

            pass

        def execute(need_active=False):
            '''Execute selected file
               Arguments:
               @need_active (bool): Only execute if there's an active selected file in the file list
                  (optional)

            '''

            pass

        def filenum(increment=1):
            '''Increment number in filename
               Arguments:
               @increment (int): in [-100, 100], (optional)

            '''

            pass

        def filepath_drop(filepath="Path"):
            '''undocumented
               Arguments:
               @filepath (str): (optional, never None)

            '''

            pass

        def find_missing_files(find_all=False, directory="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=False, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Try to find missing external files
               Arguments:
               @find_all (bool): Find all files in the search path (not just missing)
                  (optional)
               @directory (str): Directory of the file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def hidedot():
            '''Toggle hide hidden dot files
            '''

            pass

        def highlight():
            '''Highlight selected file(s)
            '''

            pass

        def make_paths_absolute():
            '''Make all paths to external files absolute
            '''

            pass

        def make_paths_relative():
            '''Make all paths to external files relative to current .blend
            '''

            pass

        def next():
            '''Move to next folder
            '''

            pass

        def pack_all():
            '''Pack all used external files into the .blend
            '''

            pass

        def pack_libraries():
            '''Pack all used Blender library files into the current .blend
            '''

            pass

        def parent():
            '''Move to parent directory
            '''

            pass

        def previous():
            '''Move to previous folder
            '''

            pass

        def refresh():
            '''Refresh the file list
            '''

            pass

        def rename():
            '''Rename file or file directory
            '''

            pass

        def report_missing_files():
            '''Report all missing external files
            '''

            pass

        def reset_recent():
            '''Reset Recent files
            '''

            pass

        def select(extend=False, fill=False, open=True):
            '''Activate/select file
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @fill (bool): Select everything beginning with the last selection
                  (optional)
               @open (bool): Open a directory when selecting it
                  (optional)

            '''

            pass

        def select_all_toggle():
            '''Select or deselect all files
            '''

            pass

        def select_bookmark(dir=""):
            '''Select a bookmarked directory
               Arguments:
               @dir (str): (optional, never None)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Activate/select the file(s) contained in the border
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_walk(direction='UP', extend=False, fill=False):
            '''Select/Deselect files by walking through them
               Arguments:
               @direction (str): Select/Deselect file in this direction
                  in ['UP', 'DOWN', 'LEFT', 'RIGHT'], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @fill (bool): Select everything beginning with the last selection
                  (optional)

            '''

            pass

        def smoothscroll():
            '''Smooth scroll to make editable file visible
            '''

            pass

        def unpack_all(method='USE_LOCAL'):
            '''Unpack all files packed into this .blend to external ones
               Arguments:
               @method (str): How to unpack
                  in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL', 'KEEP'], (optional)

            '''

            pass

        def unpack_item(method='USE_LOCAL', id_name="", id_type=19785):
            '''Unpack this file to an external file
               Arguments:
               @method (str): How to unpack
                  in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)
               @id_name (str): Name of ID block to unpack
                  (optional, never None)
               @id_type (int): Identifier type of ID block
                  in [0, inf], (optional)

            '''

            pass

        def unpack_libraries():
            '''Unpack all used Blender library files from this .blend file
            '''

            pass

    class fluid:
        '''Spcecial class, created just to reflect content of bpy.ops.fluid'''

        def bake():
            '''Bake fluid simulation
            '''

            pass

        def preset_add(name="", remove_active=False):
            '''Add or remove a Fluid Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

    class font:
        '''Spcecial class, created just to reflect content of bpy.ops.font'''

        def case_set(case='LOWER'):
            '''Set font case
               Arguments:
               @case (str): Lower or upper case
                  in ['LOWER', 'UPPER'], (optional)

            '''

            pass

        def case_toggle():
            '''Toggle font case
            '''

            pass

        def change_character(delta=1):
            '''Change font character code
               Arguments:
               @delta (int): Number to increase or decrease character code with
                  in [-255, 255], (optional)

            '''

            pass

        def change_spacing(delta=1):
            '''Change font spacing
               Arguments:
               @delta (int): Amount to decrease or increase character spacing with
                  in [-20, 20], (optional)

            '''

            pass

        def delete(type='ALL'):
            '''Delete text by cursor position
               Arguments:
               @type (str): Which part of the text to delete
                  in ['ALL', 'NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'SELECTION', 'NEXT_OR_SELECTION', 'PREVIOUS_OR_SELECTION'], (optional)

            '''

            pass

        def line_break():
            '''Insert line break at cursor position
            '''

            pass

        def move(type='LINE_BEGIN'):
            '''Move cursor to position type
               Arguments:
               @type (str): Where to move cursor to
                  in ['LINE_BEGIN', 'LINE_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)

            '''

            pass

        def move_select(type='LINE_BEGIN'):
            '''Move the cursor while selecting
               Arguments:
               @type (str): Where to move cursor to, to make a selection
                  in ['LINE_BEGIN', 'LINE_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)

            '''

            pass

        def open(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=True, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Load a new font from a file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def select_all():
            '''Select all text
            '''

            pass

        def style_set(style='BOLD', clear=False):
            '''Set font style
               Arguments:
               @style (str): Style to set selection to
                  in ['BOLD', 'ITALIC', 'UNDERLINE', 'SMALL_CAPS'], (optional)
               @clear (bool): Clear style rather than setting it
                  (optional)

            '''

            pass

        def style_toggle(style='BOLD'):
            '''Toggle font style
               Arguments:
               @style (str): Style to set selection to
                  in ['BOLD', 'ITALIC', 'UNDERLINE', 'SMALL_CAPS'], (optional)

            '''

            pass

        def text_copy():
            '''Copy selected text to clipboard
            '''

            pass

        def text_cut():
            '''Cut selected text to clipboard
            '''

            pass

        def text_insert(text="", accent=False):
            '''Insert text at cursor position
               Arguments:
               @text (str): Text to insert at the cursor position
                  (optional, never None)
               @accent (bool): Next typed character will strike through previous, for special character input
                  (optional)

            '''

            pass

        def text_paste():
            '''Paste text from clipboard
            '''

            pass

        def text_paste_from_file(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=True, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Paste contents from file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def textbox_add():
            '''Add a new text box
            '''

            pass

        def textbox_remove(index=0):
            '''Remove the textbox
               Arguments:
               @index (int): The current text box
                  in [0, inf], (optional)

            '''

            pass

        def unlink():
            '''Unlink active font data block
            '''

            pass

    class gpencil:
        '''Spcecial class, created just to reflect content of bpy.ops.gpencil'''

        def active_frame_delete():
            '''Delete the active frame for the active Grease Pencil Layer
            '''

            pass

        def active_frames_delete_all():
            '''Delete the active frame(s) of all editable Grease Pencil layers
            '''

            pass

        def brush_add():
            '''Add new Grease Pencil drawing brush for the active Grease Pencil datablock
            '''

            pass

        def brush_change(brush='DEFAULT'):
            '''Change active Grease Pencil drawing brush
               Arguments:
               @brush (str): in ['DEFAULT'], (optional)

            '''

            pass

        def brush_copy():
            '''Copy current Grease Pencil drawing brush
            '''

            pass

        def brush_move(type='UP'):
            '''Move the active Grease Pencil drawing brush up/down in the list
               Arguments:
               @type (str): in ['UP', 'DOWN'], (optional)

            '''

            pass

        def brush_paint(stroke=None, wait_for_input=True):
            '''Apply tweaks to strokes by painting over the strokes
               Arguments:
               @stroke (OperatorStrokeElement): Collection of , (optional)
               @wait_for_input (bool): Enter a mini 'sculpt-mode' if enabled, otherwise, exit after drawing a single stroke
                  (optional)

            '''

            pass

        def brush_presets_create():
            '''Create a set of predefined Grease Pencil drawing brushes
            '''

            pass

        def brush_remove():
            '''Remove active Grease Pencil drawing brush
            '''

            pass

        def brush_select(index=0):
            '''Select a Grease Pencil drawing brush
               Arguments:
               @index (int): Index of Drawing Brush
                  in [0, inf], (optional)

            '''

            pass

        def convert(type='PATH', use_normalize_weights=True, radius_multiplier=1.0, use_link_strokes=True, timing_mode='FULL', frame_range=100, start_frame=1, use_realtime=False, end_frame=250, gap_duration=0.0, gap_randomness=0.0, seed=0, use_timing_data=False):
            '''Convert the active Grease Pencil layer to a new Curve Object
               Arguments:
               @type (str): Which type of curve to convert to
                  in ['PATH', 'CURVE', 'POLY'], (optional)
               @use_normalize_weights (bool): Normalize weight (set from stroke width)
                  (optional)
               @radius_multiplier (float): Multiplier for the points' radii (set from stroke width)
                  in [0, 1000], (optional)
               @use_link_strokes (bool): Whether to link strokes with zero-radius sections of curves
                  (optional)
               @timing_mode (str): How to use timing data stored in strokes
                  in ['NONE', 'LINEAR', 'FULL', 'CUSTOMGAP'], (optional)
               @frame_range (int): The duration of evaluation of the path control curve
                  in [1, 10000], (optional)
               @start_frame (int): The start frame of the path control curve
                  in [1, 100000], (optional)
               @use_realtime (bool): Whether the path control curve reproduces the drawing in realtime, starting from Start Frame
                  (optional)
               @end_frame (int): The end frame of the path control curve (if Realtime is not set)
                  in [1, 100000], (optional)
               @gap_duration (float): Custom Gap mode: (Average) length of gaps, in frames (Note: Realtime value, will be scaled if Realtime is not set)
                  in [0, 10000], (optional)
               @gap_randomness (float): Custom Gap mode: Number of frames that gap lengths can vary
                  in [0, 10000], (optional)
               @seed (int): Custom Gap mode: Random generator seed
                  in [0, 1000], (optional)
               @use_timing_data (bool): Whether the converted Grease Pencil layer has valid timing data (internal use)
                  (optional)

            '''

            pass

        def copy():
            '''Copy selected Grease Pencil points and strokes
            '''

            pass

        def data_add():
            '''Add new Grease Pencil datablock
            '''

            pass

        def data_unlink():
            '''Unlink active Grease Pencil datablock
            '''

            pass

        def delete(type='POINTS'):
            '''Delete selected Grease Pencil strokes, vertices, or frames
               Arguments:
               @type (str): Method used for deleting Grease Pencil data
                  in ['POINTS', 'STROKES', 'FRAME'], (optional)

            '''

            pass

        def dissolve():
            '''Delete selected points without splitting strokes
            '''

            pass

        def draw(mode='DRAW', stroke=None, wait_for_input=True):
            '''Make annotations on the active data
               Arguments:
               @mode (str): Way to interpret mouse movements
                  in ['DRAW', 'DRAW_STRAIGHT', 'DRAW_POLY', 'ERASER'], (optional)
               @stroke (OperatorStrokeElement): Collection of , (optional)
               @wait_for_input (bool): Wait for first click instead of painting immediately
                  (optional)

            '''

            pass

        def duplicate():
            '''Duplicate the selected Grease Pencil strokes
            '''

            pass

        def duplicate_move(GPENCIL_OT_duplicate=None, TRANSFORM_OT_translate=None):
            '''Make copies of the selected Grease Pencil strokes and move them
               Arguments:
               @GPENCIL_OT_duplicate (GPENCIL_OT_duplicate): Duplicate the selected Grease Pencil strokes
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def editmode_toggle():
            '''Enter/Exit edit mode for Grease Pencil strokes
            '''

            pass

        def hide(unselected=False):
            '''Hide selected/unselected Grease Pencil layers
               Arguments:
               @unselected (bool): Hide unselected rather than selected layers
                  (optional)

            '''

            pass

        def layer_add():
            '''Add new Grease Pencil layer for the active Grease Pencil datablock
            '''

            pass

        def layer_change(layer='DEFAULT'):
            '''Change active Grease Pencil layer
               Arguments:
               @layer (str): in ['DEFAULT'], (optional)

            '''

            pass

        def layer_duplicate():
            '''Make a copy of the active Grease Pencil layer
            '''

            pass

        def layer_isolate(affect_visibility=False):
            '''Toggle whether the active layer is the only one that can be edited and/or visible
               Arguments:
               @affect_visibility (bool): In addition to toggling the editability, also affect the visibility
                  (optional)

            '''

            pass

        def layer_merge():
            '''Merge the current layer with the layer below
            '''

            pass

        def layer_move(type='UP'):
            '''Move the active Grease Pencil layer up/down in the list
               Arguments:
               @type (str): in ['UP', 'DOWN'], (optional)

            '''

            pass

        def layer_remove():
            '''Remove active Grease Pencil layer
            '''

            pass

        def lock_all():
            '''Lock all Grease Pencil layers to prevent them from being accidentally modified
            '''

            pass

        def move_to_layer(layer='DEFAULT'):
            '''Move selected strokes to another layer
               Arguments:
               @layer (str): in ['DEFAULT'], (optional)

            '''

            pass

        def palette_add():
            '''Add new Grease Pencil palette for the active Grease Pencil datablock
            '''

            pass

        def palette_change(palette='DEFAULT'):
            '''Change active Grease Pencil palette
               Arguments:
               @palette (str): in ['DEFAULT'], (optional)

            '''

            pass

        def palette_lock_layer():
            '''Lock and hide any color not used in any layer
            '''

            pass

        def palette_remove():
            '''Remove active Grease Pencil palette
            '''

            pass

        def palettecolor_add():
            '''Add new Grease Pencil palette color for the active Grease Pencil datablock
            '''

            pass

        def palettecolor_copy():
            '''Copy current Grease Pencil palette color
            '''

            pass

        def palettecolor_hide(unselected=False):
            '''Hide selected/unselected Grease Pencil colors
               Arguments:
               @unselected (bool): Hide unselected rather than selected colors
                  (optional)

            '''

            pass

        def palettecolor_isolate(affect_visibility=False):
            '''Toggle whether the active color is the only one that is editable and/or visible
               Arguments:
               @affect_visibility (bool): In addition to toggling the editability, also affect the visibility
                  (optional)

            '''

            pass

        def palettecolor_lock_all():
            '''Lock all Grease Pencil colors to prevent them from being accidentally modified
            '''

            pass

        def palettecolor_move(direction='UP'):
            '''Move the active Grease Pencil palette color up/down in the list
               Arguments:
               @direction (str): in ['UP', 'DOWN'], (optional)

            '''

            pass

        def palettecolor_remove():
            '''Remove active Grease Pencil palette color
            '''

            pass

        def palettecolor_reveal():
            '''Unhide all hidden Grease Pencil palette colors
            '''

            pass

        def palettecolor_select():
            '''Select all Grease Pencil strokes using current color
            '''

            pass

        def palettecolor_unlock_all():
            '''Unlock all Grease Pencil colors so that they can be edited
            '''

            pass

        def paste(type='COPY'):
            '''Paste previously copied strokes or copy and merge in active layer
               Arguments:
               @type (str): in ['COPY', 'MERGE'], (optional)

            '''

            pass

        def reproject():
            '''Reproject the selected strokes from the current viewpoint to get all points on the same plane again (e.g. to fix problems from accidental 3D cursor movement, or viewport changes)
            '''

            pass

        def reveal():
            '''Show all Grease Pencil layers
            '''

            pass

        def select(extend=False, deselect=False, toggle=False, entire_strokes=False, location=(0, 0)):
            '''Select Grease Pencil strokes and/or stroke points
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @deselect (bool): Remove from selection
                  (optional)
               @toggle (bool): Toggle the selection
                  (optional)
               @entire_strokes (bool): Select entire strokes instead of just the nearest stroke vertex
                  (optional)
               @location (int): Mouse location
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''Change selection of all Grease Pencil strokes currently visible
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select Grease Pencil strokes within a rectangular region
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_circle(x=0, y=0, radius=1, gesture_mode=0):
            '''Select Grease Pencil strokes using brush selection
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @radius (int): in [1, inf], (optional)
               @gesture_mode (int): in [-inf, inf], (optional)

            '''

            pass

        def select_first(only_selected_strokes=False, extend=False):
            '''Select first point in Grease Pencil strokes
               Arguments:
               @only_selected_strokes (bool): Only select the first point of strokes that already have points selected
                  (optional)
               @extend (bool): Extend selection instead of deselecting all other selected points
                  (optional)

            '''

            pass

        def select_grouped(type='LAYER'):
            '''Select all strokes with similar characteristics
               Arguments:
               @type (str): in ['LAYER', 'COLOR'], (optional)

            '''

            pass

        def select_lasso(path=None, deselect=False, extend=True):
            '''Select Grease Pencil strokes using lasso selection
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @deselect (bool): Deselect rather than select items
                  (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_last(only_selected_strokes=False, extend=False):
            '''Select last point in Grease Pencil strokes
               Arguments:
               @only_selected_strokes (bool): Only select the last point of strokes that already have points selected
                  (optional)
               @extend (bool): Extend selection instead of deselecting all other selected points
                  (optional)

            '''

            pass

        def select_less():
            '''Shrink sets of selected Grease Pencil points
            '''

            pass

        def select_linked():
            '''Select all points in same strokes as already selected points
            '''

            pass

        def select_more():
            '''Grow sets of selected Grease Pencil points
            '''

            pass

        def selection_opacity_toggle():
            '''Hide/Unhide selected points for Grease Pencil strokes setting alpha factor
            '''

            pass

        def snap_cursor_to_selected():
            '''Snap cursor to center of selected points
            '''

            pass

        def snap_to_cursor(use_offset=True):
            '''Snap selected points/strokes to the cursor
               Arguments:
               @use_offset (bool): Offset the entire stroke instead of selected points only
                  (optional)

            '''

            pass

        def snap_to_grid():
            '''Snap selected points to the nearest grid points
            '''

            pass

        def stroke_apply_thickness():
            '''Apply the thickness change of the layer to its strokes
            '''

            pass

        def stroke_arrange(direction='UP'):
            '''Arrange selected strokes up/down in the drawing order of the active layer
               Arguments:
               @direction (str): in ['UP', 'DOWN', 'TOP', 'BOTTOM'], (optional)

            '''

            pass

        def stroke_change_color():
            '''Move selected strokes to active color
            '''

            pass

        def stroke_cyclical_set(type='TOGGLE'):
            '''Close or open the selected stroke adding an edge from last to first point
               Arguments:
               @type (str): in ['CLOSE', 'OPEN', 'TOGGLE'], (optional)

            '''

            pass

        def stroke_flip():
            '''Change direction of the points of the selected strokes
            '''

            pass

        def stroke_join(type='JOIN', leave_gaps=False):
            '''Join selected strokes (optionally as new stroke)
               Arguments:
               @type (str): in ['JOIN', 'JOINCOPY'], (optional)
               @leave_gaps (bool): Leave gaps between joined strokes instead of linking them
                  (optional)

            '''

            pass

        def stroke_lock_color():
            '''Lock any color not used in any selected stroke
            '''

            pass

        def unlock_all():
            '''Unlock all Grease Pencil layers so that they can be edited
            '''

            pass

    class graph:
        '''Spcecial class, created just to reflect content of bpy.ops.graph'''

        def bake():
            '''Bake selected F-Curves to a set of sampled points defining a similar curve
            '''

            pass

        def clean(threshold=0.001, channels=False):
            '''Simplify F-Curves by removing closely spaced keyframes
               Arguments:
               @threshold (float): in [0, inf], (optional)
               @channels (bool): (optional)

            '''

            pass

        def click_insert(frame=1.0, value=1.0, extend=False):
            '''Insert new keyframe at the cursor position for the active F-Curve
               Arguments:
               @frame (float): Frame to insert keyframe on
                  in [-inf, inf], (optional)
               @value (float): Value for keyframe on
                  in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def clickselect(extend=False, column=False, curves=False):
            '''Select keyframes by clicking on them
               Arguments:
               @extend (bool): Toggle keyframe selection instead of leaving newly selected keyframes only
                  (optional)
               @column (bool): Select all keyframes that occur on the same frame as the one under the mouse
                  (optional)
               @curves (bool): Select all the keyframes in the curve
                  (optional)

            '''

            pass

        def copy():
            '''Copy selected keyframes to the copy/paste buffer
            '''

            pass

        def cursor_set(frame=0.0, value=0.0):
            '''Interactively set the current frame and value cursor
               Arguments:
               @frame (float): in [-500000, 500000], (optional)
               @value (float): in [-inf, inf], (optional)

            '''

            pass

        def delete():
            '''Remove all selected keyframes
            '''

            pass

        def driver_variables_copy():
            '''Copy the driver variables of the active F-Curve
            '''

            pass

        def driver_variables_paste(replace=False):
            '''Add copied driver variables to the active driver
               Arguments:
               @replace (bool): Replace existing driver variables, instead of just appending to the end of the existing list
                  (optional)

            '''

            pass

        def duplicate(mode='TRANSLATION'):
            '''Make a copy of all selected keyframes
               Arguments:
               @mode (str): in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)

            '''

            pass

        def duplicate_move(GRAPH_OT_duplicate=None, TRANSFORM_OT_transform=None):
            '''Make a copy of all selected keyframes and move them
               Arguments:
               @GRAPH_OT_duplicate (GRAPH_OT_duplicate): Make a copy of all selected keyframes
                  (optional)
               @TRANSFORM_OT_transform (TRANSFORM_OT_transform): Transform selected items by mode type
                  (optional)

            '''

            pass

        def easing_type(type='AUTO'):
            '''Set easing type for the F-Curve segments starting from the selected keyframes
               Arguments:
               @type (str): in ['AUTO', 'EASE_IN', 'EASE_OUT', 'EASE_IN_OUT'], (optional)

            '''

            pass

        def euler_filter():
            '''Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics
            '''

            pass

        def extrapolation_type(type='CONSTANT'):
            '''Set extrapolation mode for selected F-Curves
               Arguments:
               @type (str): in ['CONSTANT', 'LINEAR', 'MAKE_CYCLIC', 'CLEAR_CYCLIC'], (optional)

            '''

            pass

        def fmodifier_add(type='NULL', only_active=True):
            '''Add F-Modifier to the active/selected F-Curves
               Arguments:
               @type (str): in ['NULL', 'GENERATOR', 'FNGENERATOR', 'ENVELOPE', 'CYCLES', 'NOISE', 'LIMITS', 'STEPPED'], (optional)
               @only_active (bool): Only add F-Modifier to active F-Curve
                  (optional)

            '''

            pass

        def fmodifier_copy():
            '''Copy the F-Modifier(s) of the active F-Curve
            '''

            pass

        def fmodifier_paste(only_active=True, replace=False):
            '''Add copied F-Modifiers to the selected F-Curves
               Arguments:
               @only_active (bool): Only paste F-Modifiers on active F-Curve
                  (optional)
               @replace (bool): Replace existing F-Modifiers, instead of just appending to the end of the existing list
                  (optional)

            '''

            pass

        def frame_jump():
            '''Place the cursor on the midpoint of selected keyframes
            '''

            pass

        def ghost_curves_clear():
            '''Clear F-Curve snapshots (Ghosts) for active Graph Editor
            '''

            pass

        def ghost_curves_create():
            '''Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor
            '''

            pass

        def handle_type(type='FREE'):
            '''Set type of handle for selected keyframes
               Arguments:
               @type (str): in ['FREE', 'VECTOR', 'ALIGNED', 'AUTO', 'AUTO_CLAMPED'], (optional)

            '''

            pass

        def hide(unselected=False):
            '''Hide selected curves from Graph Editor view
               Arguments:
               @unselected (bool): Hide unselected rather than selected curves
                  (optional)

            '''

            pass

        def interpolation_type(type='CONSTANT'):
            '''Set interpolation mode for the F-Curve segments starting from the selected keyframes
               Arguments:
               @type (str): in ['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC'], (optional)

            '''

            pass

        def keyframe_insert(type='ALL'):
            '''Insert keyframes for the specified channels
               Arguments:
               @type (str): in ['ALL', 'SEL', 'CURSOR_ACTIVE', 'CURSOR_SEL'], (optional)

            '''

            pass

        def mirror(type='CFRA'):
            '''Flip selected keyframes over the selected mirror line
               Arguments:
               @type (str): in ['CFRA', 'VALUE', 'YAXIS', 'XAXIS', 'MARKER'], (optional)

            '''

            pass

        def paste(offset='START', merge='MIX', flipped=False):
            '''Paste keyframes from copy/paste buffer for the selected channels, starting on the current frame
               Arguments:
               @offset (str): Paste time offset of keys
                  in ['START', 'END', 'RELATIVE', 'NONE'], (optional)
               @merge (str): Method of merging pasted keys and existing
                  in ['MIX', 'OVER_ALL', 'OVER_RANGE', 'OVER_RANGE_ALL'], (optional)
               @flipped (bool): Paste keyframes from mirrored bones if they exist
                  (optional)

            '''

            pass

        def previewrange_set():
            '''Automatically set Preview Range based on range of keyframes
            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def reveal():
            '''Make previously hidden curves visible again in Graph Editor view
            '''

            pass

        def sample():
            '''Add keyframes on every frame between the selected keyframes
            '''

            pass

        def select_all_toggle(invert=False):
            '''Toggle selection of all keyframes
               Arguments:
               @invert (bool): (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False, include_handles=False):
            '''Select all keyframes within the specified region
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @axis_range (bool): (optional)
               @include_handles (bool): Are handles tested individually against the selection criteria
                  (optional)

            '''

            pass

        def select_circle(x=0, y=0, radius=1, gesture_mode=0):
            '''Select keyframe points using circle selection
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @radius (int): in [1, inf], (optional)
               @gesture_mode (int): in [-inf, inf], (optional)

            '''

            pass

        def select_column(mode='KEYS'):
            '''Select all keyframes on the specified frame(s)
               Arguments:
               @mode (str): in ['KEYS', 'CFRA', 'MARKERS_COLUMN', 'MARKERS_BETWEEN'], (optional)

            '''

            pass

        def select_lasso(path=None, deselect=False, extend=True):
            '''Select keyframe points using lasso selection
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @deselect (bool): Deselect rather than select items
                  (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_leftright(mode='CHECK', extend=False):
            '''Select keyframes to the left or the right of the current frame
               Arguments:
               @mode (str): in ['CHECK', 'LEFT', 'RIGHT'], (optional)
               @extend (bool): (optional)

            '''

            pass

        def select_less():
            '''Deselect keyframes on ends of selection islands
            '''

            pass

        def select_linked():
            '''Select keyframes occurring in the same F-Curves as selected ones
            '''

            pass

        def select_more():
            '''Select keyframes beside already selected ones
            '''

            pass

        def smooth():
            '''Apply weighted moving means to make selected F-Curves less bumpy
            '''

            pass

        def snap(type='CFRA'):
            '''Snap selected keyframes to the chosen times/values
               Arguments:
               @type (str): in ['CFRA', 'VALUE', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER', 'HORIZONTAL'], (optional)

            '''

            pass

        def sound_bake(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', low=0.0, high=100000.0, attack=0.005, release=0.2, threshold=0.0, use_accumulate=False, use_additive=False, use_square=False, sthreshold=0.1):
            '''Bakes a sound wave to selected F-Curves
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @low (float): Cutoff frequency of a high-pass filter that is applied to the audio data
                  in [0, 100000], (optional)
               @high (float): Cutoff frequency of a low-pass filter that is applied to the audio data
                  in [0, 100000], (optional)
               @attack (float): Value for the hull curve calculation that tells how fast the hull curve can rise (the lower the value the steeper it can rise)
                  in [0, 2], (optional)
               @release (float): Value for the hull curve calculation that tells how fast the hull curve can fall (the lower the value the steeper it can fall)
                  in [0, 5], (optional)
               @threshold (float): Minimum amplitude value needed to influence the hull curve
                  in [0, 1], (optional)
               @use_accumulate (bool): Only the positive differences of the hull curve amplitudes are summarized to produce the output
                  (optional)
               @use_additive (bool): The amplitudes of the hull curve are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)
                  (optional)
               @use_square (bool): The output is a square curve (negative values always result in -1, and positive ones in 1)
                  (optional)
               @sthreshold (float): Square only: all values with an absolute amplitude lower than that result in 0
                  in [0, 1], (optional)

            '''

            pass

        def view_all(include_handles=True):
            '''Reset viewable area to show full keyframe range
               Arguments:
               @include_handles (bool): Include handles of keyframes when calculating extents
                  (optional)

            '''

            pass

        def view_frame():
            '''Reset viewable area to show range around current frame
            '''

            pass

        def view_selected(include_handles=True):
            '''Reset viewable area to show selected keyframe range
               Arguments:
               @include_handles (bool): Include handles of keyframes when calculating extents
                  (optional)

            '''

            pass

    class group:
        '''Spcecial class, created just to reflect content of bpy.ops.group'''

        def create(name="Group"):
            '''Create an object group from selected objects
               Arguments:
               @name (str): Name of the new group
                  (optional, never None)

            '''

            pass

        def objects_add_active(group=''):
            '''Add the object to an object group that contains the active object
               Arguments:
               @group (str): The group to add other selected objects to
                  in [], (optional)

            '''

            pass

        def objects_remove(group=''):
            '''Remove selected objects from a group
               Arguments:
               @group (str): The group to remove this object from
                  in [], (optional)

            '''

            pass

        def objects_remove_active(group=''):
            '''Remove the object from an object group that contains the active object
               Arguments:
               @group (str): The group to remove other selected objects from
                  in [], (optional)

            '''

            pass

        def objects_remove_all():
            '''Remove selected objects from all groups
            '''

            pass

    class image:
        '''Spcecial class, created just to reflect content of bpy.ops.image'''

        def change_frame(frame=0):
            '''Interactively change the current frame number
               Arguments:
               @frame (int): in [-500000, 500000], (optional)

            '''

            pass

        def clear_render_border():
            '''Clear the boundaries of the border render and disable border render
            '''

            pass

        def curves_point_set(point='BLACK_POINT'):
            '''Set black point or white point for curves
               Arguments:
               @point (str): Set black point or white point for curves
                  in ['BLACK_POINT', 'WHITE_POINT'], (optional)

            '''

            pass

        def cycle_render_slot(reverse=False):
            '''Cycle through all non-void render slots
               Arguments:
               @reverse (bool): (optional)

            '''

            pass

        def external_edit(filepath=""):
            '''Edit image in an external application
               Arguments:
               @filepath (str): (optional, never None)

            '''

            pass

        def invert(invert_r=False, invert_g=False, invert_b=False, invert_a=False):
            '''Invert image's channels
               Arguments:
               @invert_r (bool): Invert Red Channel
                  (optional)
               @invert_g (bool): Invert Green Channel
                  (optional)
               @invert_b (bool): Invert Blue Channel
                  (optional)
               @invert_a (bool): Invert Alpha Channel
                  (optional)

            '''

            pass

        def match_movie_length():
            '''Set image's user's length to the one of this video
            '''

            pass

        def new(name="Untitled", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False, gen_context='NONE', use_stereo_3d=False):
            '''Create a new image
               Arguments:
               @name (str): Image datablock name
                  (optional, never None)
               @width (int): Image width
                  in [1, inf], (optional)
               @height (int): Image height
                  in [1, inf], (optional)
               @color (float): Default fill color
                  array of 4 items in [0, inf], (optional)
               @alpha (bool): Create an image with an alpha channel
                  (optional)
               @generated_type (str): Fill the image with a grid for UV map testing
                  in ['BLANK', 'UV_GRID', 'COLOR_GRID'], (optional)
               @float (bool): Create image with 32 bit floating point bit depth
                  (optional)
               @gen_context (str): Generation context
                  in ['NONE', 'PAINT_CANVAS', 'PAINT_STENCIL'], (optional)
               @use_stereo_3d (bool): Create an image with left and right views
                  (optional)

            '''

            pass

        def open(filepath="", directory="", files=None, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Open image
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @directory (str): Directory of the file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def pack(as_png=False):
            '''Pack an image as embedded data into the .blend file
               Arguments:
               @as_png (bool): Pack image as lossless PNG
                  (optional)

            '''

            pass

        def project_apply():
            '''Project edited image back onto the object
            '''

            pass

        def project_edit():
            '''Edit a snapshot of the view-port in an external image editor
            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def read_renderlayers():
            '''Read all the current scene's render layers from cache, as needed
            '''

            pass

        def reload():
            '''Reload current image from disk
            '''

            pass

        def render_border(xmin=0, xmax=0, ymin=0, ymax=0):
            '''Set the boundaries of the border render and enable border render
               Arguments:
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def replace(filepath="", filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Replace current image by another one from disk
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def sample():
            '''Use mouse to sample a color in current image
            '''

            pass

        def sample_line(xstart=0, xend=0, ystart=0, yend=0, cursor=1002):
            '''Sample a line and show it in Scope panels
               Arguments:
               @xstart (int): in [-inf, inf], (optional)
               @xend (int): in [-inf, inf], (optional)
               @ystart (int): in [-inf, inf], (optional)
               @yend (int): in [-inf, inf], (optional)
               @cursor (int): Mouse cursor style to use during the modal operator
                  in [0, inf], (optional)

            '''

            pass

        def save():
            '''Save the image with current name and settings
            '''

            pass

        def save_as(save_as_render=False, copy=False, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Save the image with another name and/or settings
               Arguments:
               @save_as_render (bool): Apply render part of display transform when saving byte image
                  (optional)
               @copy (bool): Create a new image file without modifying the current image in blender
                  (optional)
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def save_dirty():
            '''Save all modified textures
            '''

            pass

        def save_sequence():
            '''Save a sequence of images
            '''

            pass

        def toolshelf():
            '''Toggles tool shelf display
            '''

            pass

        def unpack(method='USE_LOCAL', id=""):
            '''Save an image packed in the .blend file to disk
               Arguments:
               @method (str): How to unpack
                  in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)
               @id (str): Image datablock name to unpack
                  (optional, never None)

            '''

            pass

        def view_all(fit_view=False):
            '''View the entire image
               Arguments:
               @fit_view (bool): Fit frame to the viewport
                  (optional)

            '''

            pass

        def view_ndof():
            '''Use a 3D mouse device to pan/zoom the view
            '''

            pass

        def view_pan(offset=(0.0, 0.0)):
            '''Pan the view
               Arguments:
               @offset (float): Offset in floating point units, 1.0 is the width and height of the image
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def view_selected():
            '''View all selected UVs
            '''

            pass

        def view_zoom(factor=0.0):
            '''Zoom in/out the image
               Arguments:
               @factor (float): Zoom factor, values higher than 1.0 zoom in, lower values zoom out
                  in [-inf, inf], (optional)

            '''

            pass

        def view_zoom_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
            '''Zoom in the view to the nearest item contained in the border
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def view_zoom_in(location=(0.0, 0.0)):
            '''Zoom in the image (centered around 2D cursor)
               Arguments:
               @location (float): Cursor location in screen coordinates
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def view_zoom_out(location=(0.0, 0.0)):
            '''Zoom out the image (centered around 2D cursor)
               Arguments:
               @location (float): Cursor location in screen coordinates
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def view_zoom_ratio(ratio=0.0):
            '''Set zoom ratio of the view
               Arguments:
               @ratio (float): Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
                  in [-inf, inf], (optional)

            '''

            pass

    class import_anim:
        '''Spcecial class, created just to reflect content of bpy.ops.import_anim'''

        def bvh(filepath="", axis_forward='-Z', axis_up='Y', filter_glob="*.bvh", target='ARMATURE', global_scale=1.0, frame_start=1, use_fps_scale=False, update_scene_fps=False, update_scene_duration=False, use_cyclic=False, rotate_mode='NATIVE'):
            '''Load a BVH motion capture file
               Arguments:
               @filepath (str): Filepath used for importing the file
                  (optional, never None)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @target (str): Import target type
                  in ['ARMATURE', 'OBJECT'], (optional)
               @global_scale (float): Scale the BVH by this value
                  in [0.0001, 1e+06], (optional)
               @frame_start (int): Starting frame for the animation
                  in [-inf, inf], (optional)
               @use_fps_scale (bool): Scale the framerate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame
                  (optional)
               @update_scene_fps (bool): Set the scene framerate to that of the BVH file (note that this nullifies the 'Scale FPS' option, as the scale will be 1:1)
                  (optional)
               @update_scene_duration (bool): Extend the scene's duration to the BVH duration (never shortens the scene)
                  (optional)
               @use_cyclic (bool): Loop the animation playback
                  (optional)
               @rotate_mode (str): Rotation conversion
                  in ['QUATERNION', 'NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'], (optional)

            '''

            pass

    class import_curve:
        '''Spcecial class, created just to reflect content of bpy.ops.import_curve'''

        def svg(filepath="", filter_glob="*.svg"):
            '''Load a SVG file
               Arguments:
               @filepath (str): Filepath used for importing the file
                  (optional, never None)
               @filter_glob (str): (optional, never None)

            '''

            pass

    class import_image:
        '''Spcecial class, created just to reflect content of bpy.ops.import_image'''

        def to_plane(rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), view_align=False, location=(0.0, 0.0, 0.0), files=None, directory="", filter_image=True, filter_movie=True, filter_folder=True, filter_glob="", align=True, align_offset=0.1, force_reload=False, extension='*', size_mode='ABSOLUTE', height=1.0, factor=600.0, use_shadeless=False, use_transparency=False, transparency_method='MASK', use_transparent_shadows=False, shader='BSDF_DIFFUSE', overwrite_node_tree=True, alpha_mode='STRAIGHT', match_len=True, use_fields=False, use_auto_refresh=True, relative=True):
            '''Create mesh plane(s) from image files with the appropiate aspect ratio
               Arguments:
               @rotation (float): array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)
               @view_align (bool): (optional)
               @location (float): array of 3 items in [-inf, inf], (optional)
               @files (OperatorFileListElement): Collection of , (optional)
               @directory (str): (optional, never None)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_glob (str): (optional, never None)
               @align (bool): Create Planes in a row
                  (optional)
               @align_offset (float): Space between Planes
                  in [0, inf], (optional)
               @force_reload (bool): Force reloading of the image if already opened elsewhere in Blender
                  (optional)
               @extension (str): Only import files of this type
                  in ['*', 'jpeg', 'png', 'tga', 'tiff', 'bmp', 'cin', 'dpx', 'psd', 'exr', 'hdr', 'avi', 'mov', 'mp4', 'ogg'], (optional)
               @size_mode (str): How the size of the plane is computed
                  in ['ABSOLUTE', 'DPI', 'DPBU'], (optional)
               @height (float): Height of the created plane
                  in [0.001, inf], (optional)
               @factor (float): Number of pixels per inch or Blender Unit
                  in [1, inf], (optional)
               @use_shadeless (bool): Make this material insensitive to light or shadow
                  (optional)
               @use_transparency (bool): Use alphachannel for transparency
                  (optional)
               @transparency_method (str): Method to use for rendering transparency
                  in ['MASK', 'Z_TRANSPARENCY', 'RAYTRACE'], (optional)
               @use_transparent_shadows (bool): Allow this object to receive transparent shadows cast through other objects
                  (optional)
               @shader (str): Node shader to use
                  in ['BSDF_DIFFUSE', 'EMISSION'], (optional)
               @overwrite_node_tree (bool): Overwrite existing Material with new nodetree (based on material name)
                  (optional)
               @alpha_mode (str): Representation of alpha information in the RGBA pixels
                  in ['STRAIGHT', 'PREMUL'], (optional)
               @match_len (bool): Set image's user's length to the one of this video
                  (optional)
               @use_fields (bool): Use fields of the image
                  (optional)
               @use_auto_refresh (bool): Always refresh image on frame changes
                  (optional)
               @relative (bool): Apply relative paths
                  (optional)

            '''

            pass

    class import_mesh:
        '''Spcecial class, created just to reflect content of bpy.ops.import_mesh'''

        def ply(filepath="", files=None, directory="", filter_glob="*.ply"):
            '''Load a PLY geometry file
               Arguments:
               @filepath (str): Filepath used for importing the file
                  (optional, never None)
               @files (OperatorFileListElement): File path used for importing the PLY file
                  Collection of , (optional)
               @directory (str): (optional, never None)
               @filter_glob (str): (optional, never None)

            '''

            pass

        def stl(filepath="", axis_forward='Y', axis_up='Z', filter_glob="*.stl", files=None, directory="", global_scale=1.0, use_scene_unit=False, use_facet_normal=False):
            '''Load STL triangle mesh data
               Arguments:
               @filepath (str): Filepath used for importing the file
                  (optional, never None)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @directory (str): (optional, never None)
               @global_scale (float): in [1e-06, 1e+06], (optional)
               @use_scene_unit (bool): Apply current scene's unit (as defined by unit scale) to imported data
                  (optional)
               @use_facet_normal (bool): Use (import) facet normals (note that this will still give flat shading)
                  (optional)

            '''

            pass

    class import_scene:
        '''Spcecial class, created just to reflect content of bpy.ops.import_scene'''

        def autodesk_3ds(filepath="", axis_forward='Y', axis_up='Z', filter_glob="*.3ds", constrain_size=10.0, use_image_search=True, use_apply_transform=True):
            '''Import from 3DS file format (.3ds)
               Arguments:
               @filepath (str): Filepath used for importing the file
                  (optional, never None)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @constrain_size (float): Scale the model by 10 until it reaches the size constraint (0 to disable)
                  in [0, 1000], (optional)
               @use_image_search (bool): Search subdirectories for any associated images (Warning, may be slow)
                  (optional)
               @use_apply_transform (bool): Workaround for object transformations importing incorrectly
                  (optional)

            '''

            pass

        def fbx(filepath="", axis_forward='-Z', axis_up='Y', directory="", filter_glob="*.fbx", ui_tab='MAIN', use_manual_orientation=False, global_scale=1.0, bake_space_transform=False, use_custom_normals=True, use_image_search=True, use_alpha_decals=False, decal_offset=0.0, use_anim=True, anim_offset=1.0, use_custom_props=True, use_custom_props_enum_as_string=True, ignore_leaf_bones=False, force_connect_children=False, automatic_bone_orientation=False, primary_bone_axis='Y', secondary_bone_axis='X', use_prepost_rot=True):
            '''Load a FBX file
               Arguments:
               @filepath (str): Filepath used for importing the file
                  (optional, never None)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @directory (str): (optional, never None)
               @filter_glob (str): (optional, never None)
               @ui_tab (str): Import options categories
                  in ['MAIN', 'ARMATURE'], (optional)
               @use_manual_orientation (bool): Specify orientation and scale, instead of using embedded data in FBX file
                  (optional)
               @global_scale (float): in [0.001, 1000], (optional)
               @bake_space_transform (bool): Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
                  (optional)
               @use_custom_normals (bool): Import custom normals, if available (otherwise Blender will recompute them)
                  (optional)
               @use_image_search (bool): Search subdirs for any associated images (WARNING: may be slow)
                  (optional)
               @use_alpha_decals (bool): Treat materials with alpha as decals (no shadow casting)
                  (optional)
               @decal_offset (float): Displace geometry of alpha meshes
                  in [0, 1], (optional)
               @use_anim (bool): Import FBX animation
                  (optional)
               @anim_offset (float): Offset to apply to animation during import, in frames
                  in [-inf, inf], (optional)
               @use_custom_props (bool): Import user properties as custom properties
                  (optional)
               @use_custom_props_enum_as_string (bool): Store enumeration values as strings
                  (optional)
               @ignore_leaf_bones (bool): Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
                  (optional)
               @force_connect_children (bool): Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
                  (optional)
               @automatic_bone_orientation (bool): Try to align the major bone axis with the bone children
                  (optional)
               @primary_bone_axis (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @secondary_bone_axis (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @use_prepost_rot (bool): Use pre/post rotation from FBX transform (you may have to disable that in some cases)
                  (optional)

            '''

            pass

        def obj(filepath="", axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True, use_groups_as_vgroups=False, use_image_search=True, split_mode='ON', global_clamp_size=0.0):
            '''Load a Wavefront OBJ File
               Arguments:
               @filepath (str): Filepath used for importing the file
                  (optional, never None)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)
               @use_edges (bool): Import lines and faces with 2 verts as edge
                  (optional)
               @use_smooth_groups (bool): Surround smooth groups by sharp edges
                  (optional)
               @use_split_objects (bool): Import OBJ Objects into Blender Objects
                  (optional)
               @use_split_groups (bool): Import OBJ Groups into Blender Objects
                  (optional)
               @use_groups_as_vgroups (bool): Import OBJ groups as vertex groups
                  (optional)
               @use_image_search (bool): Search subdirs for any associated images (Warning, may be slow)
                  (optional)
               @split_mode (str): in ['ON', 'OFF'], (optional)
               @global_clamp_size (float): Clamp bounds under this value (zero to disable)
                  in [0, 1000], (optional)

            '''

            pass

        def x3d(filepath="", axis_forward='Z', axis_up='Y', filter_glob="*.x3d;*.wrl"):
            '''Import an X3D or VRML2 file
               Arguments:
               @filepath (str): Filepath used for importing the file
                  (optional, never None)
               @axis_forward (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @axis_up (str): in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
               @filter_glob (str): (optional, never None)

            '''

            pass

    class info:
        '''Spcecial class, created just to reflect content of bpy.ops.info'''

        def report_copy():
            '''Copy selected reports to Clipboard
            '''

            pass

        def report_delete():
            '''Delete selected reports
            '''

            pass

        def report_replay():
            '''Replay selected reports
            '''

            pass

        def reports_display_update():
            '''Update the display of reports in Blender UI (internal use)
            '''

            pass

        def select_all_toggle():
            '''Select or deselect all reports
            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Toggle border selection
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_pick(report_index=0):
            '''Select reports by index
               Arguments:
               @report_index (int): Index of the report
                  in [0, inf], (optional)

            '''

            pass

    class lamp:
        '''Spcecial class, created just to reflect content of bpy.ops.lamp'''

        def sunsky_preset_add(name="", remove_active=False):
            '''Add or remove a Sky & Atmosphere Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

    class lattice:
        '''Spcecial class, created just to reflect content of bpy.ops.lattice'''

        def flip(axis='U'):
            '''Mirror all control points without inverting the lattice deform
               Arguments:
               @axis (str): Coordinates along this axis get flipped
                  in ['U', 'V', 'W'], (optional)

            '''

            pass

        def make_regular():
            '''Set UVW control points a uniform distance apart
            '''

            pass

        def select_all(action='TOGGLE'):
            '''Change selection of all UVW control points
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_less():
            '''Deselect vertices at the boundary of each selection region
            '''

            pass

        def select_mirror(axis={'X'}, extend=False):
            '''Select mirrored lattice points
               Arguments:
               @axis (str): set in {'X', 'Y', 'Z'}, (optional)
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_more():
            '''Select vertex directly linked to already selected ones
            '''

            pass

        def select_random(percent=50.0, seed=0, action='SELECT'):
            '''Randomly select UVW control points
               Arguments:
               @percent (float): Percentage of objects to select randomly
                  in [0, 100], (optional)
               @seed (int): Seed for the random number generator
                  in [0, inf], (optional)
               @action (str): Selection action to execute
                  in ['SELECT', 'DESELECT'], (optional)

            '''

            pass

        def select_ungrouped(extend=False):
            '''Select vertices without a group
               Arguments:
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

    class logic:
        '''Spcecial class, created just to reflect content of bpy.ops.logic'''

        def actuator_add(type='', name="", object=""):
            '''Add an actuator to the active object
               Arguments:
               @type (str): Type of actuator to add
                  in [], (optional)
               @name (str): Name of the Actuator to add
                  (optional, never None)
               @object (str): Name of the Object to add the Actuator to
                  (optional, never None)

            '''

            pass

        def actuator_move(actuator="", object="", direction='UP'):
            '''Move Actuator
               Arguments:
               @actuator (str): Name of the actuator to edit
                  (optional, never None)
               @object (str): Name of the object the actuator belongs to
                  (optional, never None)
               @direction (str): Move Up or Down
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def actuator_remove(actuator="", object=""):
            '''Remove an actuator from the active object
               Arguments:
               @actuator (str): Name of the actuator to edit
                  (optional, never None)
               @object (str): Name of the object the actuator belongs to
                  (optional, never None)

            '''

            pass

        def controller_add(type='LOGIC_AND', name="", object=""):
            '''Add a controller to the active object
               Arguments:
               @type (str): Type of controller to add
                  in ['LOGIC_AND', 'LOGIC_OR', 'LOGIC_NAND', 'LOGIC_NOR', 'LOGIC_XOR', 'LOGIC_XNOR', 'EXPRESSION', 'PYTHON'], (optional)
               @name (str): Name of the Controller to add
                  (optional, never None)
               @object (str): Name of the Object to add the Controller to
                  (optional, never None)

            '''

            pass

        def controller_move(controller="", object="", direction='UP'):
            '''Move Controller
               Arguments:
               @controller (str): Name of the controller to edit
                  (optional, never None)
               @object (str): Name of the object the controller belongs to
                  (optional, never None)
               @direction (str): Move Up or Down
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def controller_remove(controller="", object=""):
            '''Remove a controller from the active object
               Arguments:
               @controller (str): Name of the controller to edit
                  (optional, never None)
               @object (str): Name of the object the controller belongs to
                  (optional, never None)

            '''

            pass

        def links_cut(path=None, cursor=9):
            '''Remove logic brick connections
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @cursor (int): in [0, inf], (optional)

            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def sensor_add(type='', name="", object=""):
            '''Add a sensor to the active object
               Arguments:
               @type (str): Type of sensor to add
                  in [], (optional)
               @name (str): Name of the Sensor to add
                  (optional, never None)
               @object (str): Name of the Object to add the Sensor to
                  (optional, never None)

            '''

            pass

        def sensor_move(sensor="", object="", direction='UP'):
            '''Move Sensor
               Arguments:
               @sensor (str): Name of the sensor to edit
                  (optional, never None)
               @object (str): Name of the object the sensor belongs to
                  (optional, never None)
               @direction (str): Move Up or Down
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def sensor_remove(sensor="", object=""):
            '''Remove a sensor from the active object
               Arguments:
               @sensor (str): Name of the sensor to edit
                  (optional, never None)
               @object (str): Name of the object the sensor belongs to
                  (optional, never None)

            '''

            pass

        def view_all():
            '''Resize view so you can see all logic bricks
            '''

            pass

    class marker:
        '''Spcecial class, created just to reflect content of bpy.ops.marker'''

        def add():
            '''Add a new time marker
            '''

            pass

        def camera_bind():
            '''Bind the active camera to selected marker(s)
            '''

            pass

        def delete():
            '''Delete selected time marker(s)
            '''

            pass

        def duplicate(frames=0):
            '''Duplicate selected time marker(s)
               Arguments:
               @frames (int): in [-inf, inf], (optional)

            '''

            pass

        def make_links_scene(scene=''):
            '''Copy selected markers to another scene
               Arguments:
               @scene (str): in [], (optional)

            '''

            pass

        def move(frames=0):
            '''Move selected time marker(s)
               Arguments:
               @frames (int): in [-inf, inf], (optional)

            '''

            pass

        def rename(name="RenamedMarker"):
            '''Rename first selected time marker
               Arguments:
               @name (str): New name for marker
                  (optional, never None)

            '''

            pass

        def select(extend=False, camera=False):
            '''Select time marker(s)
               Arguments:
               @extend (bool): Extend the selection
                  (optional)
               @camera (bool): Select the camera
                  (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''Change selection of all time markers
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select all time markers using border selection
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

    class mask:
        '''Spcecial class, created just to reflect content of bpy.ops.mask'''

        def add_feather_vertex(location=(0.0, 0.0)):
            '''Add vertex to feather
               Arguments:
               @location (float): Location of vertex in normalized space
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def add_feather_vertex_slide(MASK_OT_add_feather_vertex=None, MASK_OT_slide_point=None):
            '''Add new vertex to feather and slide it
               Arguments:
               @MASK_OT_add_feather_vertex (MASK_OT_add_feather_vertex): Add vertex to feather
                  (optional)
               @MASK_OT_slide_point (MASK_OT_slide_point): Slide control points
                  (optional)

            '''

            pass

        def add_vertex(location=(0.0, 0.0)):
            '''Add vertex to active spline
               Arguments:
               @location (float): Location of vertex in normalized space
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def add_vertex_slide(MASK_OT_add_vertex=None, MASK_OT_slide_point=None):
            '''Add new vertex and slide it
               Arguments:
               @MASK_OT_add_vertex (MASK_OT_add_vertex): Add vertex to active spline
                  (optional)
               @MASK_OT_slide_point (MASK_OT_slide_point): Slide control points
                  (optional)

            '''

            pass

        def copy_splines():
            '''Copy selected splines to clipboard
            '''

            pass

        def cyclic_toggle():
            '''Toggle cyclic for selected splines
            '''

            pass

        def delete():
            '''Delete selected control points or splines
            '''

            pass

        def duplicate():
            '''Duplicate selected control points and segments between them
            '''

            pass

        def duplicate_move(MASK_OT_duplicate=None, TRANSFORM_OT_translate=None):
            '''Duplicate mask and move
               Arguments:
               @MASK_OT_duplicate (MASK_OT_duplicate): Duplicate selected control points and segments between them
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def feather_weight_clear():
            '''Reset the feather weight to zero
            '''

            pass

        def handle_type_set(type='AUTO'):
            '''Set type of handles for selected control points
               Arguments:
               @type (str): Spline type
                  in ['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE'], (optional)

            '''

            pass

        def hide_view_clear():
            '''Reveal the layer by setting the hide flag
            '''

            pass

        def hide_view_set(unselected=False):
            '''Hide the layer by setting the hide flag
               Arguments:
               @unselected (bool): Hide unselected rather than selected layers
                  (optional)

            '''

            pass

        def layer_move(direction='UP'):
            '''Move the active layer up/down in the list
               Arguments:
               @direction (str): Direction to move the active layer
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def layer_new(name=""):
            '''Add new mask layer for masking
               Arguments:
               @name (str): Name of new mask layer
                  (optional, never None)

            '''

            pass

        def layer_remove():
            '''Remove mask layer
            '''

            pass

        def new(name=""):
            '''Create new mask
               Arguments:
               @name (str): Name of new mask
                  (optional, never None)

            '''

            pass

        def normals_make_consistent():
            '''Re-calculate the direction of selected handles
            '''

            pass

        def parent_clear():
            '''Clear the mask's parenting
            '''

            pass

        def parent_set():
            '''Set the mask's parenting
            '''

            pass

        def paste_splines():
            '''Paste splines from clipboard
            '''

            pass

        def primitive_circle_add(size=100.0, location=(0.0, 0.0)):
            '''Add new circle-shaped spline
               Arguments:
               @size (float): Size of new circle
                  in [-inf, inf], (optional)
               @location (float): Location of new circle
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def primitive_square_add(size=100.0, location=(0.0, 0.0)):
            '''Add new square-shaped spline
               Arguments:
               @size (float): Size of new circle
                  in [-inf, inf], (optional)
               @location (float): Location of new circle
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def select(extend=False, deselect=False, toggle=False, location=(0.0, 0.0)):
            '''Select spline points
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @deselect (bool): Remove from selection
                  (optional)
               @toggle (bool): Toggle the selection
                  (optional)
               @location (float): Location of vertex in normalized space
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''Change selection of all curve points
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select curve points using border selection
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_circle(x=0, y=0, radius=1, gesture_mode=0):
            '''Select curve points using circle selection
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @radius (int): in [1, inf], (optional)
               @gesture_mode (int): in [-inf, inf], (optional)

            '''

            pass

        def select_lasso(path=None, deselect=False, extend=True):
            '''Select curve points using lasso selection
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @deselect (bool): Deselect rather than select items
                  (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_less():
            '''Deselect spline points at the boundary of each selection region
            '''

            pass

        def select_linked():
            '''Select all curve points linked to already selected ones
            '''

            pass

        def select_linked_pick(deselect=False):
            '''(De)select all points linked to the curve under the mouse cursor
               Arguments:
               @deselect (bool): (optional)

            '''

            pass

        def select_more():
            '''Select more spline points connected to initial selection
            '''

            pass

        def shape_key_clear():
            '''undocumented
            '''

            pass

        def shape_key_feather_reset():
            '''Reset feather weights on all selected points animation values
            '''

            pass

        def shape_key_insert():
            '''undocumented
            '''

            pass

        def shape_key_rekey(location=True, feather=True):
            '''Recalculate animation data on selected points for frames selected in the dopesheet
               Arguments:
               @location (bool): (optional)
               @feather (bool): (optional)

            '''

            pass

        def slide_point(slide_feather=False, is_new_point=False):
            '''Slide control points
               Arguments:
               @slide_feather (bool): First try to slide feather instead of vertex
                  (optional)
               @is_new_point (bool): Newly created vertex is being slid
                  (optional)

            '''

            pass

        def slide_spline_curvature():
            '''Slide a point on the spline to define it's curvature
            '''

            pass

        def switch_direction():
            '''Switch direction of selected splines
            '''

            pass

    class material:
        '''Spcecial class, created just to reflect content of bpy.ops.material'''

        def copy():
            '''Copy the material settings and nodes
            '''

            pass

        def new():
            '''Add a new material
            '''

            pass

        def paste():
            '''Paste the material settings and nodes
            '''

            pass

        def sss_preset_add(name="", remove_active=False):
            '''Add or remove a Subsurface Scattering Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

    class mball:
        '''Spcecial class, created just to reflect content of bpy.ops.mball'''

        def delete_metaelems():
            '''Delete selected metaelement(s)
            '''

            pass

        def duplicate_metaelems():
            '''Duplicate selected metaelement(s)
            '''

            pass

        def duplicate_move(MBALL_OT_duplicate_metaelems=None, TRANSFORM_OT_translate=None):
            '''Make copies of the selected metaelements and move them
               Arguments:
               @MBALL_OT_duplicate_metaelems (MBALL_OT_duplicate_metaelems): Duplicate selected metaelement(s)
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def hide_metaelems(unselected=False):
            '''Hide (un)selected metaelement(s)
               Arguments:
               @unselected (bool): Hide unselected rather than selected
                  (optional)

            '''

            pass

        def reveal_metaelems():
            '''Reveal all hidden metaelements
            '''

            pass

        def select_all(action='TOGGLE'):
            '''Change selection of all meta elements
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_random_metaelems(percent=50.0, seed=0, action='SELECT'):
            '''Randomly select metaelements
               Arguments:
               @percent (float): Percentage of objects to select randomly
                  in [0, 100], (optional)
               @seed (int): Seed for the random number generator
                  in [0, inf], (optional)
               @action (str): Selection action to execute
                  in ['SELECT', 'DESELECT'], (optional)

            '''

            pass

        def select_similar(type='TYPE', threshold=0.1):
            '''Select similar metaballs by property types
               Arguments:
               @type (str): in ['TYPE', 'RADIUS', 'STIFFNESS', 'ROTATION'], (optional)
               @threshold (float): in [0, 1], (optional)

            '''

            pass

    class mesh:
        '''Spcecial class, created just to reflect content of bpy.ops.mesh'''

        def beautify_fill(angle_limit=3.14159):
            '''Rearrange some faces to try to get less degenerated geometry
               Arguments:
               @angle_limit (float): Angle limit
                  in [0, 3.14159], (optional)

            '''

            pass

        def bevel(offset_type='OFFSET', offset=0.0, segments=1, profile=0.5, vertex_only=False, clamp_overlap=False, loop_slide=True, material=-1):
            '''Edge Bevel
               Arguments:
               @offset_type (str): What distance Amount measures
                  in ['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT'], (optional)
               @offset (float): in [-1e+06, 1e+06], (optional)
               @segments (int): Segments for curved edge
                  in [1, 1000], (optional)
               @profile (float): Controls profile shape (0.5 = round)
                  in [0.15, 1], (optional)
               @vertex_only (bool): Bevel only vertices
                  (optional)
               @clamp_overlap (bool): Do not allow beveled edges/vertices to overlap each other
                  (optional)
               @loop_slide (bool): Prefer slide along edge to even widths
                  (optional)
               @material (int): Material for bevel faces (-1 means use adjacent faces)
                  in [-1, inf], (optional)

            '''

            pass

        def bisect(plane_co=(0.0, 0.0, 0.0), plane_no=(0.0, 0.0, 0.0), use_fill=False, clear_inner=False, clear_outer=False, threshold=0.0001, xstart=0, xend=0, ystart=0, yend=0, cursor=1002):
            '''Cut geometry along a plane (click-drag to define plane)
               Arguments:
               @plane_co (float): A point on the plane
                  array of 3 items in [-inf, inf], (optional)
               @plane_no (float): The direction the plane points
                  array of 3 items in [-1, 1], (optional)
               @use_fill (bool): Fill in the cut
                  (optional)
               @clear_inner (bool): Remove geometry behind the plane
                  (optional)
               @clear_outer (bool): Remove geometry in front of the plane
                  (optional)
               @threshold (float): in [0, 10], (optional)
               @xstart (int): in [-inf, inf], (optional)
               @xend (int): in [-inf, inf], (optional)
               @ystart (int): in [-inf, inf], (optional)
               @yend (int): in [-inf, inf], (optional)
               @cursor (int): Mouse cursor style to use during the modal operator
                  in [0, inf], (optional)

            '''

            pass

        def blend_from_shape(shape='', blend=1.0, add=True):
            '''Blend in shape from a shape key
               Arguments:
               @shape (str): Shape key to use for blending
                  in [], (optional)
               @blend (float): Blending factor
                  in [-1000, 1000], (optional)
               @add (bool): Add rather than blend between shapes
                  (optional)

            '''

            pass

        def bridge_edge_loops(type='SINGLE', use_merge=False, merge_factor=0.5, twist_offset=0, number_cuts=0, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH'):
            '''Make faces between two or more edge loops
               Arguments:
               @type (str): Method of bridging multiple loops
                  in ['SINGLE', 'CLOSED', 'PAIRS'], (optional)
               @use_merge (bool): Merge rather than creating faces
                  (optional)
               @merge_factor (float): in [0, 1], (optional)
               @twist_offset (int): Twist offset for closed loops
                  in [-1000, 1000], (optional)
               @number_cuts (int): in [0, 1000], (optional)
               @interpolation (str): Interpolation method
                  in ['LINEAR', 'PATH', 'SURFACE'], (optional)
               @smoothness (float): Smoothness factor
                  in [0, 1000], (optional)
               @profile_shape_factor (float): How much intermediary new edges are shrunk/expanded
                  in [-1000, 1000], (optional)
               @profile_shape (str): Shape of the profile
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional)

            '''

            pass

        def colors_reverse():
            '''Flip direction of vertex colors inside faces
            '''

            pass

        def colors_rotate(use_ccw=False):
            '''Rotate vertex colors inside faces
               Arguments:
               @use_ccw (bool): (optional)

            '''

            pass

        def convex_hull(delete_unused=True, use_existing_faces=True, make_holes=False, join_triangles=True, face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False):
            '''Enclose selected vertices in a convex polyhedron
               Arguments:
               @delete_unused (bool): Delete selected elements that are not used by the hull
                  (optional)
               @use_existing_faces (bool): Skip hull triangles that are covered by a pre-existing face
                  (optional)
               @make_holes (bool): Delete selected faces that are used by the hull
                  (optional)
               @join_triangles (bool): Merge adjacent triangles into quads
                  (optional)
               @face_threshold (float): Face angle limit
                  in [0, 3.14159], (optional)
               @shape_threshold (float): Shape angle limit
                  in [0, 3.14159], (optional)
               @uvs (bool): (optional)
               @vcols (bool): (optional)
               @seam (bool): (optional)
               @sharp (bool): (optional)
               @materials (bool): (optional)

            '''

            pass

        def customdata_custom_splitnormals_add():
            '''Add a custom split normals layer, if none exists yet
            '''

            pass

        def customdata_custom_splitnormals_clear():
            '''Remove the custom split normals layer, if it exists
            '''

            pass

        def customdata_mask_clear():
            '''Clear vertex sculpt masking data from the mesh
            '''

            pass

        def customdata_skin_add():
            '''Add a vertex skin layer
            '''

            pass

        def customdata_skin_clear():
            '''Clear vertex skin layer
            '''

            pass

        def decimate(ratio=1.0, use_vertex_group=False, vertex_group_factor=1.0, invert_vertex_group=False, use_symmetry=False, symmetry_axis='Y'):
            '''Simplify geometry by collapsing edges
               Arguments:
               @ratio (float): in [0, 1], (optional)
               @use_vertex_group (bool): Use active vertex group as an influence
                  (optional)
               @vertex_group_factor (float): Vertex group strength
                  in [0, 1000], (optional)
               @invert_vertex_group (bool): Invert vertex group influence
                  (optional)
               @use_symmetry (bool): Maintain symmetry on an axis
                  (optional)
               @symmetry_axis (str): Axis of symmetry
                  in ['X', 'Y', 'Z'], (optional)

            '''

            pass

        def delete(type='VERT'):
            '''Delete selected vertices, edges or faces
               Arguments:
               @type (str): Method used for deleting mesh data
                  in ['VERT', 'EDGE', 'FACE', 'EDGE_FACE', 'ONLY_FACE'], (optional)

            '''

            pass

        def delete_edgeloop(use_face_split=True):
            '''Delete an edge loop by merging the faces on each side
               Arguments:
               @use_face_split (bool): Split off face corners to maintain surrounding geometry
                  (optional)

            '''

            pass

        def delete_loose(use_verts=True, use_edges=True, use_faces=False):
            '''Delete loose vertices, edges or faces
               Arguments:
               @use_verts (bool): Remove loose vertices
                  (optional)
               @use_edges (bool): Remove loose edges
                  (optional)
               @use_faces (bool): Remove loose faces
                  (optional)

            '''

            pass

        def dissolve_degenerate(threshold=0.0001):
            '''Dissolve zero area faces and zero length edges
               Arguments:
               @threshold (float): Minimum distance between elements to merge
                  in [1e-06, 50], (optional)

            '''

            pass

        def dissolve_edges(use_verts=True, use_face_split=False):
            '''Dissolve edges, merging faces
               Arguments:
               @use_verts (bool): Dissolve remaining vertices
                  (optional)
               @use_face_split (bool): Split off face corners to maintain surrounding geometry
                  (optional)

            '''

            pass

        def dissolve_faces(use_verts=False):
            '''Dissolve faces
               Arguments:
               @use_verts (bool): Dissolve remaining vertices
                  (optional)

            '''

            pass

        def dissolve_limited(angle_limit=0.0872665, use_dissolve_boundaries=False, delimit={'NORMAL'}):
            '''Dissolve selected edges and verts, limited by the angle of surrounding geometry
               Arguments:
               @angle_limit (float): Angle limit
                  in [0, 3.14159], (optional)
               @use_dissolve_boundaries (bool): Dissolve all vertices inbetween face boundaries
                  (optional)
               @delimit (str): Delimit dissolve operation
                  set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional)

            '''

            pass

        def dissolve_mode(use_verts=False, use_face_split=False, use_boundary_tear=False):
            '''Dissolve geometry based on the selection mode
               Arguments:
               @use_verts (bool): Dissolve remaining vertices
                  (optional)
               @use_face_split (bool): Split off face corners to maintain surrounding geometry
                  (optional)
               @use_boundary_tear (bool): Split off face corners instead of merging faces
                  (optional)

            '''

            pass

        def dissolve_verts(use_face_split=False, use_boundary_tear=False):
            '''Dissolve verts, merge edges and faces
               Arguments:
               @use_face_split (bool): Split off face corners to maintain surrounding geometry
                  (optional)
               @use_boundary_tear (bool): Split off face corners instead of merging faces
                  (optional)

            '''

            pass

        def drop_named_image(name="Image", filepath="Path", relative_path=True):
            '''Assign Image to active UV Map, or create an UV Map
               Arguments:
               @name (str): Image name to assign
                  (optional, never None)
               @filepath (str): Path to image file
                  (optional, never None)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)

            '''

            pass

        def dupli_extrude_cursor(rotate_source=True):
            '''Duplicate and extrude selected vertices, edges or faces towards the mouse cursor
               Arguments:
               @rotate_source (bool): Rotate initial selection giving better shape
                  (optional)

            '''

            pass

        def duplicate(mode=1):
            '''Duplicate selected vertices, edges or faces
               Arguments:
               @mode (int): in [0, inf], (optional)

            '''

            pass

        def duplicate_move(MESH_OT_duplicate=None, TRANSFORM_OT_translate=None):
            '''Duplicate mesh and move
               Arguments:
               @MESH_OT_duplicate (MESH_OT_duplicate): Duplicate selected vertices, edges or faces
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def edge_collapse():
            '''Collapse selected edges
            '''

            pass

        def edge_face_add():
            '''Add an edge or face to selected
            '''

            pass

        def edge_rotate(use_ccw=False):
            '''Rotate selected edge or adjoining faces
               Arguments:
               @use_ccw (bool): (optional)

            '''

            pass

        def edge_split():
            '''Split selected edges so that each neighbor face gets its own copy
            '''

            pass

        def edgering_select(extend=False, deselect=False, toggle=False, ring=True):
            '''Select an edge ring
               Arguments:
               @extend (bool): Extend the selection
                  (optional)
               @deselect (bool): Remove from the selection
                  (optional)
               @toggle (bool): Toggle the selection
                  (optional)
               @ring (bool): Select ring
                  (optional)

            '''

            pass

        def edges_select_sharp(sharpness=0.523599):
            '''Select all sharp-enough edges
               Arguments:
               @sharpness (float): in [0.000174533, 3.14159], (optional)

            '''

            pass

        def extrude_edges_indiv(mirror=False):
            '''Extrude individual edges only
               Arguments:
               @mirror (bool): (optional)

            '''

            pass

        def extrude_edges_move(MESH_OT_extrude_edges_indiv=None, TRANSFORM_OT_translate=None):
            '''Extrude edges and move result
               Arguments:
               @MESH_OT_extrude_edges_indiv (MESH_OT_extrude_edges_indiv): Extrude individual edges only
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def extrude_faces_indiv(mirror=False):
            '''Extrude individual faces only
               Arguments:
               @mirror (bool): (optional)

            '''

            pass

        def extrude_faces_move(MESH_OT_extrude_faces_indiv=None, TRANSFORM_OT_shrink_fatten=None):
            '''Extrude faces and move result
               Arguments:
               @MESH_OT_extrude_faces_indiv (MESH_OT_extrude_faces_indiv): Extrude individual faces only
                  (optional)
               @TRANSFORM_OT_shrink_fatten (TRANSFORM_OT_shrink_fatten): Shrink/fatten selected vertices along normals
                  (optional)

            '''

            pass

        def extrude_region(mirror=False):
            '''Extrude region of faces
               Arguments:
               @mirror (bool): (optional)

            '''

            pass

        def extrude_region_move(MESH_OT_extrude_region=None, TRANSFORM_OT_translate=None):
            '''Extrude region and move result
               Arguments:
               @MESH_OT_extrude_region (MESH_OT_extrude_region): Extrude region of faces
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def extrude_region_shrink_fatten(MESH_OT_extrude_region=None, TRANSFORM_OT_shrink_fatten=None):
            '''Extrude region and move result
               Arguments:
               @MESH_OT_extrude_region (MESH_OT_extrude_region): Extrude region of faces
                  (optional)
               @TRANSFORM_OT_shrink_fatten (TRANSFORM_OT_shrink_fatten): Shrink/fatten selected vertices along normals
                  (optional)

            '''

            pass

        def extrude_repeat(offset=2.0, steps=10):
            '''Extrude selected vertices, edges or faces repeatedly
               Arguments:
               @offset (float): in [0, inf], (optional)
               @steps (int): in [0, 1000000], (optional)

            '''

            pass

        def extrude_vertices_move(MESH_OT_extrude_verts_indiv=None, TRANSFORM_OT_translate=None):
            '''Extrude vertices and move result
               Arguments:
               @MESH_OT_extrude_verts_indiv (MESH_OT_extrude_verts_indiv): Extrude individual vertices only
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def extrude_verts_indiv(mirror=False):
            '''Extrude individual vertices only
               Arguments:
               @mirror (bool): (optional)

            '''

            pass

        def face_make_planar(factor=1.0, repeat=1):
            '''Flatten selected faces
               Arguments:
               @factor (float): in [-10, 10], (optional)
               @repeat (int): in [1, 10000], (optional)

            '''

            pass

        def face_split_by_edges():
            '''Weld loose edges into faces (splitting them into new faces)
            '''

            pass

        def faces_mirror_uv(direction='POSITIVE', precision=3):
            '''Copy mirror UV coordinates on the X axis based on a mirrored mesh
               Arguments:
               @direction (str): in ['POSITIVE', 'NEGATIVE'], (optional)
               @precision (int): Tolerance for finding vertex duplicates
                  in [1, 16], (optional)

            '''

            pass

        def faces_select_linked_flat(sharpness=0.0174533):
            '''Select linked faces by angle
               Arguments:
               @sharpness (float): in [0.000174533, 3.14159], (optional)

            '''

            pass

        def faces_shade_flat():
            '''Display faces flat
            '''

            pass

        def faces_shade_smooth():
            '''Display faces smooth (using vertex normals)
            '''

            pass

        def fill(use_beauty=True):
            '''Fill a selected edge loop with faces
               Arguments:
               @use_beauty (bool): Use best triangulation division
                  (optional)

            '''

            pass

        def fill_grid(span=1, offset=0, use_interp_simple=False):
            '''Fill grid from two loops
               Arguments:
               @span (int): Number of sides (zero disables)
                  in [1, 1000], (optional)
               @offset (int): Number of sides (zero disables)
                  in [-1000, 1000], (optional)
               @use_interp_simple (bool): (optional)

            '''

            pass

        def fill_holes(sides=4):
            '''Fill in holes (boundary edge loops)
               Arguments:
               @sides (int): Number of sides in hole required to fill (zero fills all holes)
                  in [0, 1000], (optional)

            '''

            pass

        def flip_normals():
            '''Flip the direction of selected faces' normals (and of their vertices)
            '''

            pass

        def hide(unselected=False):
            '''Hide (un)selected vertices, edges or faces
               Arguments:
               @unselected (bool): Hide unselected rather than selected
                  (optional)

            '''

            pass

        def inset(use_boundary=True, use_even_offset=True, use_relative_offset=False, use_edge_rail=False, thickness=0.01, depth=0.0, use_outset=False, use_select_inset=False, use_individual=False, use_interpolate=True):
            '''Inset new faces into selected faces
               Arguments:
               @use_boundary (bool): Inset face boundaries
                  (optional)
               @use_even_offset (bool): Scale the offset to give more even thickness
                  (optional)
               @use_relative_offset (bool): Scale the offset by surrounding geometry
                  (optional)
               @use_edge_rail (bool): Inset the region along existing edges
                  (optional)
               @thickness (float): in [0, inf], (optional)
               @depth (float): in [-inf, inf], (optional)
               @use_outset (bool): Outset rather than inset
                  (optional)
               @use_select_inset (bool): Select the new inset faces
                  (optional)
               @use_individual (bool): Individual Face Inset
                  (optional)
               @use_interpolate (bool): Blend face data across the inset
                  (optional)

            '''

            pass

        def intersect(mode='SELECT_UNSELECT', use_separate=True, threshold=1e-06):
            '''Cut an intersection into faces
               Arguments:
               @mode (str): in ['SELECT', 'SELECT_UNSELECT'], (optional)
               @use_separate (bool): (optional)
               @threshold (float): in [0, 0.01], (optional)

            '''

            pass

        def intersect_boolean(operation='DIFFERENCE', use_swap=False, threshold=1e-06):
            '''Cut solid geometry from selected to unselected
               Arguments:
               @operation (str): in ['INTERSECT', 'UNION', 'DIFFERENCE'], (optional)
               @use_swap (bool): Use with difference intersection to swap which side is kept
                  (optional)
               @threshold (float): in [0, 0.01], (optional)

            '''

            pass

        def knife_project(cut_through=False):
            '''Use other objects outlines & boundaries to project knife cuts
               Arguments:
               @cut_through (bool): Cut through all faces, not just visible ones
                  (optional)

            '''

            pass

        def knife_tool(use_occlude_geometry=True, only_selected=False):
            '''Cut new topology
               Arguments:
               @use_occlude_geometry (bool): Only cut the front most geometry
                  (optional)
               @only_selected (bool): Only cut selected geometry
                  (optional)

            '''

            pass

        def loop_multi_select(ring=False):
            '''Select a loop of connected edges by connection type
               Arguments:
               @ring (bool): (optional)

            '''

            pass

        def loop_select(extend=False, deselect=False, toggle=False, ring=False):
            '''Select a loop of connected edges
               Arguments:
               @extend (bool): Extend the selection
                  (optional)
               @deselect (bool): Remove from the selection
                  (optional)
               @toggle (bool): Toggle the selection
                  (optional)
               @ring (bool): Select ring
                  (optional)

            '''

            pass

        def loop_to_region(select_bigger=False):
            '''Select region of faces inside of a selected loop of edges
               Arguments:
               @select_bigger (bool): Select bigger regions instead of smaller ones
                  (optional)

            '''

            pass

        def loopcut(number_cuts=1, smoothness=0.0, falloff='INVERSE_SQUARE', edge_index=-1, mesh_select_mode_init=(False, False, False)):
            '''Add a new loop between existing loops
               Arguments:
               @number_cuts (int): in [1, 1000000], (optional)
               @smoothness (float): Smoothness factor
                  in [-1000, 1000], (optional)
               @falloff (str): Falloff type the feather
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional)
               @edge_index (int): in [-1, inf], (optional)
               @mesh_select_mode_init (bool): array of 3 items, (optional)

            '''

            pass

        def loopcut_slide(MESH_OT_loopcut=None, TRANSFORM_OT_edge_slide=None):
            '''Cut mesh loop and slide it
               Arguments:
               @MESH_OT_loopcut (MESH_OT_loopcut): Add a new loop between existing loops
                  (optional)
               @TRANSFORM_OT_edge_slide (TRANSFORM_OT_edge_slide): Slide an edge loop along a mesh
                  (optional)

            '''

            pass

        def mark_freestyle_edge(clear=False):
            '''(Un)mark selected edges as Freestyle feature edges
               Arguments:
               @clear (bool): (optional)

            '''

            pass

        def mark_freestyle_face(clear=False):
            '''(Un)mark selected faces for exclusion from Freestyle feature edge detection
               Arguments:
               @clear (bool): (optional)

            '''

            pass

        def mark_seam(clear=False):
            '''(Un)mark selected edges as a seam
               Arguments:
               @clear (bool): (optional)

            '''

            pass

        def mark_sharp(clear=False, use_verts=False):
            '''(Un)mark selected edges as sharp
               Arguments:
               @clear (bool): (optional)
               @use_verts (bool): Consider vertices instead of edges to select which edges to (un)tag as sharp
                  (optional)

            '''

            pass

        def merge(type='CENTER', uvs=False):
            '''Merge selected vertices
               Arguments:
               @type (str): Merge method to use
                  in ['FIRST', 'LAST', 'CENTER', 'CURSOR', 'COLLAPSE'], (optional)
               @uvs (bool): Move UVs according to merge
                  (optional)

            '''

            pass

        def navmesh_clear():
            '''Remove navmesh data from this mesh
            '''

            pass

        def navmesh_face_add():
            '''Add a new index and assign it to selected faces
            '''

            pass

        def navmesh_face_copy():
            '''Copy the index from the active face
            '''

            pass

        def navmesh_make():
            '''Create navigation mesh for selected objects
            '''

            pass

        def navmesh_reset():
            '''Assign a new index to every face
            '''

            pass

        def noise(factor=0.1):
            '''Use vertex coordinate as texture coordinate
               Arguments:
               @factor (float): in [-10000, 10000], (optional)

            '''

            pass

        def normals_make_consistent(inside=False):
            '''Make face and vertex normals point either outside or inside the mesh
               Arguments:
               @inside (bool): (optional)

            '''

            pass

        def offset_edge_loops(use_cap_endpoint=False):
            '''Create offset edge loop from the current selection
               Arguments:
               @use_cap_endpoint (bool): Extend loop around end-points
                  (optional)

            '''

            pass

        def offset_edge_loops_slide(MESH_OT_offset_edge_loops=None, TRANSFORM_OT_edge_slide=None):
            '''Offset edge loop slide
               Arguments:
               @MESH_OT_offset_edge_loops (MESH_OT_offset_edge_loops): Create offset edge loop from the current selection
                  (optional)
               @TRANSFORM_OT_edge_slide (TRANSFORM_OT_edge_slide): Slide an edge loop along a mesh
                  (optional)

            '''

            pass

        def poke(offset=0.0, use_relative_offset=False, center_mode='MEAN_WEIGHTED'):
            '''Split a face into a fan
               Arguments:
               @offset (float): Poke Offset
                  in [-1000, 1000], (optional)
               @use_relative_offset (bool): Scale the offset by surrounding geometry
                  (optional)
               @center_mode (str): Poke Face Center Calculation
                  in ['MEAN_WEIGHTED', 'MEAN', 'BOUNDS'], (optional)

            '''

            pass

        def primitive_circle_add(vertices=32, radius=1.0, fill_type='NOTHING', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a circle mesh
               Arguments:
               @vertices (int): in [3, 10000000], (optional)
               @radius (float): in [0, inf], (optional)
               @fill_type (str): in ['NOTHING', 'NGON', 'TRIFAN'], (optional)
               @calc_uvs (bool): Generate a default UV map
                  (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_cone_add(vertices=32, radius1=1.0, radius2=0.0, depth=2.0, end_fill_type='NGON', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a conic mesh
               Arguments:
               @vertices (int): in [3, 10000000], (optional)
               @radius1 (float): in [0, inf], (optional)
               @radius2 (float): in [0, inf], (optional)
               @depth (float): in [0, inf], (optional)
               @end_fill_type (str): in ['NOTHING', 'NGON', 'TRIFAN'], (optional)
               @calc_uvs (bool): Generate a default UV map
                  (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_cube_add(radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a cube mesh
               Arguments:
               @radius (float): in [0, inf], (optional)
               @calc_uvs (bool): Generate a default UV map
                  (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_cylinder_add(vertices=32, radius=1.0, depth=2.0, end_fill_type='NGON', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a cylinder mesh
               Arguments:
               @vertices (int): in [3, 10000000], (optional)
               @radius (float): in [0, inf], (optional)
               @depth (float): in [0, inf], (optional)
               @end_fill_type (str): in ['NOTHING', 'NGON', 'TRIFAN'], (optional)
               @calc_uvs (bool): Generate a default UV map
                  (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_grid_add(x_subdivisions=10, y_subdivisions=10, radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a grid mesh
               Arguments:
               @x_subdivisions (int): in [2, 10000000], (optional)
               @y_subdivisions (int): in [2, 10000000], (optional)
               @radius (float): in [0, inf], (optional)
               @calc_uvs (bool): Generate a default UV map
                  (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_ico_sphere_add(subdivisions=2, size=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct an Icosphere mesh
               Arguments:
               @subdivisions (int): in [1, 10], (optional)
               @size (float): in [0, inf], (optional)
               @calc_uvs (bool): Generate a default UV map
                  (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_monkey_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Suzanne mesh
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_plane_add(radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a filled planar mesh with 4 vertices
               Arguments:
               @radius (float): in [0, inf], (optional)
               @calc_uvs (bool): Generate a default UV map
                  (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_torus_add(rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), view_align=False, location=(0.0, 0.0, 0.0), major_segments=48, minor_segments=12, mode='MAJOR_MINOR', major_radius=1.0, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75):
            '''Add a torus mesh
               Arguments:
               @rotation (float): array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)
               @view_align (bool): (optional)
               @location (float): array of 3 items in [-inf, inf], (optional)
               @major_segments (int): Number of segments for the main ring of the torus
                  in [3, 256], (optional)
               @minor_segments (int): Number of segments for the minor ring of the torus
                  in [3, 256], (optional)
               @mode (str): in ['MAJOR_MINOR', 'EXT_INT'], (optional)
               @major_radius (float): Radius from the origin to the center of the cross sections
                  in [0.01, 100], (optional)
               @minor_radius (float): Radius of the torus' cross section
                  in [0.01, 100], (optional)
               @abso_major_rad (float): Total Exterior Radius of the torus
                  in [0.01, 100], (optional)
               @abso_minor_rad (float): Total Interior Radius of the torus
                  in [0.01, 100], (optional)

            '''

            pass

        def primitive_uv_sphere_add(segments=32, ring_count=16, size=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a UV sphere mesh
               Arguments:
               @segments (int): in [3, 100000], (optional)
               @ring_count (int): in [3, 100000], (optional)
               @size (float): in [0, inf], (optional)
               @calc_uvs (bool): Generate a default UV map
                  (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY'):
            '''Triangulate selected faces
               Arguments:
               @quad_method (str): Method for splitting the quads into triangles
                  in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL'], (optional)
               @ngon_method (str): Method for splitting the polygons into triangles
                  in ['BEAUTY', 'CLIP'], (optional)

            '''

            pass

        def region_to_loop():
            '''Select boundary edges around the selected faces
            '''

            pass

        def remove_doubles(threshold=0.0001, use_unselected=False):
            '''Remove duplicate vertices
               Arguments:
               @threshold (float): Minimum distance between elements to merge
                  in [1e-06, 50], (optional)
               @use_unselected (bool): Merge selected to other unselected vertices
                  (optional)

            '''

            pass

        def reveal():
            '''Reveal all hidden vertices, edges and faces
            '''

            pass

        def rip(mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=False, use_fill=False):
            '''Disconnect vertex or edges from connected geometry
               Arguments:
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)
               @use_fill (bool): Fill the ripped region
                  (optional)

            '''

            pass

        def rip_edge(mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=False):
            '''Extend vertices along the edge closest to the cursor
               Arguments:
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def rip_edge_move(MESH_OT_rip_edge=None, TRANSFORM_OT_translate=None):
            '''Extend vertices and move the result
               Arguments:
               @MESH_OT_rip_edge (MESH_OT_rip_edge): Extend vertices along the edge closest to the cursor
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def rip_move(MESH_OT_rip=None, TRANSFORM_OT_translate=None):
            '''Rip polygons and move the result
               Arguments:
               @MESH_OT_rip (MESH_OT_rip): Disconnect vertex or edges from connected geometry
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def rip_move_fill(MESH_OT_rip=None, TRANSFORM_OT_translate=None):
            '''Rip-fill polygons and move the result
               Arguments:
               @MESH_OT_rip (MESH_OT_rip): Disconnect vertex or edges from connected geometry
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def screw(steps=9, turns=1, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
            '''Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport
               Arguments:
               @steps (int): Steps
                  in [1, 100000], (optional)
               @turns (int): Turns
                  in [1, 100000], (optional)
               @center (float): Center in global view space
                  array of 3 items in [-inf, inf], (optional)
               @axis (float): Axis in global view space
                  array of 3 items in [-1, 1], (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''(De)select all vertices, edges or faces
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_axis(mode='POSITIVE', axis='X_AXIS', threshold=0.0001):
            '''Select all data in the mesh on a single axis
               Arguments:
               @mode (str): Axis side to use when selecting
                  in ['POSITIVE', 'NEGATIVE', 'ALIGNED'], (optional)
               @axis (str): Select the axis to compare each vertex on
                  in ['X_AXIS', 'Y_AXIS', 'Z_AXIS'], (optional)
               @threshold (float): in [1e-06, 50], (optional)

            '''

            pass

        def select_face_by_sides(number=4, type='EQUAL', extend=True):
            '''Select vertices or faces by the number of polygon sides
               Arguments:
               @number (int): in [3, inf], (optional)
               @type (str): Type of comparison to make
                  in ['LESS', 'EQUAL', 'GREATER', 'NOTEQUAL'], (optional)
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_interior_faces():
            '''Select faces where all edges have more than 2 face users
            '''

            pass

        def select_less(use_face_step=True):
            '''Deselect vertices, edges or faces at the boundary of each selection region
               Arguments:
               @use_face_step (bool): Connected faces (instead of edges)
                  (optional)

            '''

            pass

        def select_linked(delimit={'SEAM'}):
            '''Select all vertices linked to the active mesh
               Arguments:
               @delimit (str): Delimit selected region
                  set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional)

            '''

            pass

        def select_linked_pick(deselect=False, delimit={'SEAM'}, index=-1):
            '''(De)select all vertices linked to the edge under the mouse cursor
               Arguments:
               @deselect (bool): (optional)
               @delimit (str): Delimit selected region
                  set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional)
               @index (int): in [-1, inf], (optional)

            '''

            pass

        def select_loose(extend=False):
            '''Select loose geometry based on the selection mode
               Arguments:
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_mirror(axis={'X'}, extend=False):
            '''Select mesh items at mirrored locations
               Arguments:
               @axis (str): set in {'X', 'Y', 'Z'}, (optional)
               @extend (bool): Extend the existing selection
                  (optional)

            '''

            pass

        def select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE'):
            '''Change selection mode
               Arguments:
               @use_extend (bool): (optional)
               @use_expand (bool): (optional)
               @type (str): in ['VERT', 'EDGE', 'FACE'], (optional)
               @action (str): Selection action to execute
                  in ['DISABLE', 'ENABLE', 'TOGGLE'], (optional)

            '''

            pass

        def select_more(use_face_step=True):
            '''Select more vertices, edges or faces connected to initial selection
               Arguments:
               @use_face_step (bool): Connected faces (instead of edges)
                  (optional)

            '''

            pass

        def select_next_item():
            '''Select the next element (using selection order)
            '''

            pass

        def select_non_manifold(extend=True, use_wire=True, use_boundary=True, use_multi_face=True, use_non_contiguous=True, use_verts=True):
            '''Select all non-manifold vertices or edges
               Arguments:
               @extend (bool): Extend the selection
                  (optional)
               @use_wire (bool): Wire edges
                  (optional)
               @use_boundary (bool): Boundary edges
                  (optional)
               @use_multi_face (bool): Edges shared by 3+ faces
                  (optional)
               @use_non_contiguous (bool): Edges between faces pointing in alternate directions
                  (optional)
               @use_verts (bool): Vertices connecting multiple face regions
                  (optional)

            '''

            pass

        def select_nth(nth=2, skip=1, offset=0):
            '''Deselect every Nth element starting from the active vertex, edge or face
               Arguments:
               @nth (int): in [2, inf], (optional)
               @skip (int): in [1, inf], (optional)
               @offset (int): in [-inf, inf], (optional)

            '''

            pass

        def select_prev_item():
            '''Select the next element (using selection order)
            '''

            pass

        def select_random(percent=50.0, seed=0, action='SELECT'):
            '''Randomly select vertices
               Arguments:
               @percent (float): Percentage of objects to select randomly
                  in [0, 100], (optional)
               @seed (int): Seed for the random number generator
                  in [0, inf], (optional)
               @action (str): Selection action to execute
                  in ['SELECT', 'DESELECT'], (optional)

            '''

            pass

        def select_similar(type='NORMAL', compare='EQUAL', threshold=0.0):
            '''Select similar vertices, edges or faces by property types
               Arguments:
               @type (str): in ['NORMAL', 'FACE', 'VGROUP', 'EDGE', 'LENGTH', 'DIR', 'FACE', 'FACE_ANGLE', 'CREASE', 'BEVEL', 'SEAM', 'SHARP', 'FREESTYLE_EDGE', 'MATERIAL', 'IMAGE', 'AREA', 'SIDES', 'PERIMETER', 'NORMAL', 'COPLANAR', 'SMOOTH', 'FREESTYLE_FACE'], (optional)
               @compare (str): in ['EQUAL', 'GREATER', 'LESS'], (optional)
               @threshold (float): in [0, 1], (optional)

            '''

            pass

        def select_similar_region():
            '''Select similar face regions to the current selection
            '''

            pass

        def select_ungrouped(extend=False):
            '''Select vertices without a group
               Arguments:
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def separate(type='SELECTED'):
            '''Separate selected geometry into a new mesh
               Arguments:
               @type (str): in ['SELECTED', 'MATERIAL', 'LOOSE'], (optional)

            '''

            pass

        def shape_propagate_to_all():
            '''Apply selected vertex locations to all other shape keys
            '''

            pass

        def shortest_path_pick(use_face_step=False, use_topology_distance=False, use_fill=False, nth=1, skip=1, offset=0, index=-1):
            '''Select shortest path between two selections
               Arguments:
               @use_face_step (bool): Traverse connected faces (includes diagonals and edge-rings)
                  (optional)
               @use_topology_distance (bool): Find the minimum number of steps, ignoring spatial distance
                  (optional)
               @use_fill (bool): Select all paths between the source/destination elements
                  (optional)
               @nth (int): in [1, inf], (optional)
               @skip (int): in [1, inf], (optional)
               @offset (int): in [-inf, inf], (optional)
               @index (int): in [-1, inf], (optional)

            '''

            pass

        def shortest_path_select(use_face_step=False, use_topology_distance=False, use_fill=False, nth=1, skip=1, offset=0):
            '''Selected vertex path between two vertices
               Arguments:
               @use_face_step (bool): Traverse connected faces (includes diagonals and edge-rings)
                  (optional)
               @use_topology_distance (bool): Find the minimum number of steps, ignoring spatial distance
                  (optional)
               @use_fill (bool): Select all paths between the source/destination elements
                  (optional)
               @nth (int): in [1, inf], (optional)
               @skip (int): in [1, inf], (optional)
               @offset (int): in [-inf, inf], (optional)

            '''

            pass

        def solidify(thickness=0.01):
            '''Create a solid skin by extruding, compensating for sharp angles
               Arguments:
               @thickness (float): in [-10000, 10000], (optional)

            '''

            pass

        def sort_elements(type='VIEW_ZAXIS', elements={'VERT'}, reverse=False, seed=0):
            '''The order of selected vertices/edges/faces is modified, based on a given method
               Arguments:
               @type (str): Type of re-ordering operation to apply
                  in ['VIEW_ZAXIS', 'VIEW_XAXIS', 'CURSOR_DISTANCE', 'MATERIAL', 'SELECTED', 'RANDOMIZE', 'REVERSE'], (optional)
               @elements (str): Which elements to affect (vertices, edges and/or faces)
                  set in {'VERT', 'EDGE', 'FACE'}, (optional)
               @reverse (bool): Reverse the sorting effect
                  (optional)
               @seed (int): Seed for random-based operations
                  in [0, inf], (optional)

            '''

            pass

        def spin(steps=9, dupli=False, angle=1.5708, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
            '''Extrude selected vertices in a circle around the cursor in indicated viewport
               Arguments:
               @steps (int): Steps
                  in [0, 1000000], (optional)
               @dupli (bool): Make Duplicates
                  (optional)
               @angle (float): Rotation for each step
                  in [-inf, inf], (optional)
               @center (float): Center in global view space
                  array of 3 items in [-inf, inf], (optional)
               @axis (float): Axis in global view space
                  array of 3 items in [-1, 1], (optional)

            '''

            pass

        def split():
            '''Split off selected geometry from connected unselected geometry
            '''

            pass

        def subdivide(number_cuts=1, smoothness=0.0, quadtri=False, quadcorner='STRAIGHT_CUT', fractal=0.0, fractal_along_normal=0.0, seed=0):
            '''Subdivide selected edges
               Arguments:
               @number_cuts (int): in [1, 100], (optional)
               @smoothness (float): Smoothness factor
                  in [0, 1000], (optional)
               @quadtri (bool): Tries to prevent ngons
                  (optional)
               @quadcorner (str): How to subdivide quad corners (anything other than Straight Cut will prevent ngons)
                  in ['INNERVERT', 'PATH', 'STRAIGHT_CUT', 'FAN'], (optional)
               @fractal (float): Fractal randomness factor
                  in [0, 1e+06], (optional)
               @fractal_along_normal (float): Apply fractal displacement along normal only
                  in [0, 1], (optional)
               @seed (int): Seed for the random number generator
                  in [0, inf], (optional)

            '''

            pass

        def subdivide_edgering(number_cuts=10, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH'):
            '''undocumented
               Arguments:
               @number_cuts (int): in [0, 1000], (optional)
               @interpolation (str): Interpolation method
                  in ['LINEAR', 'PATH', 'SURFACE'], (optional)
               @smoothness (float): Smoothness factor
                  in [0, 1000], (optional)
               @profile_shape_factor (float): How much intermediary new edges are shrunk/expanded
                  in [-1000, 1000], (optional)
               @profile_shape (str): Shape of the profile
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional)

            '''

            pass

        def symmetrize(direction='NEGATIVE_X', threshold=0.0001):
            '''Enforce symmetry (both form and topological) across an axis
               Arguments:
               @direction (str): Which sides to copy from and to
                  in ['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], (optional)
               @threshold (float): in [0, 10], (optional)

            '''

            pass

        def symmetry_snap(direction='NEGATIVE_X', threshold=0.05, factor=0.5, use_center=True):
            '''Snap vertex pairs to their mirrored locations
               Arguments:
               @direction (str): Which sides to copy from and to
                  in ['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], (optional)
               @threshold (float): in [0, 10], (optional)
               @factor (float): in [0, 1], (optional)
               @use_center (bool): Snap mid verts to the axis center
                  (optional)

            '''

            pass

        def tris_convert_to_quads(face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False):
            '''Join triangles into quads
               Arguments:
               @face_threshold (float): Face angle limit
                  in [0, 3.14159], (optional)
               @shape_threshold (float): Shape angle limit
                  in [0, 3.14159], (optional)
               @uvs (bool): (optional)
               @vcols (bool): (optional)
               @seam (bool): (optional)
               @sharp (bool): (optional)
               @materials (bool): (optional)

            '''

            pass

        def unsubdivide(iterations=2):
            '''UnSubdivide selected edges & faces
               Arguments:
               @iterations (int): Number of times to unsubdivide
                  in [1, 1000], (optional)

            '''

            pass

        def uv_texture_add():
            '''Add UV Map
            '''

            pass

        def uv_texture_remove():
            '''Remove UV Map
            '''

            pass

        def uvs_reverse():
            '''Flip direction of UV coordinates inside faces
            '''

            pass

        def uvs_rotate(use_ccw=False):
            '''Rotate UV coordinates inside faces
               Arguments:
               @use_ccw (bool): (optional)

            '''

            pass

        def vert_connect():
            '''Connect selected vertices of faces, splitting the face
            '''

            pass

        def vert_connect_concave():
            '''Make all faces convex
            '''

            pass

        def vert_connect_nonplanar(angle_limit=0.0872665):
            '''Split non-planar faces that exceed the angle threshold
               Arguments:
               @angle_limit (float): Angle limit
                  in [0, 3.14159], (optional)

            '''

            pass

        def vert_connect_path():
            '''Connect vertices by their selection order, creating edges, splitting faces
            '''

            pass

        def vertex_color_add():
            '''Add vertex color layer
            '''

            pass

        def vertex_color_remove():
            '''Remove vertex color layer
            '''

            pass

        def vertices_smooth(factor=0.5, repeat=1, xaxis=True, yaxis=True, zaxis=True):
            '''Flatten angles of selected vertices
               Arguments:
               @factor (float): Smoothing factor
                  in [-10, 10], (optional)
               @repeat (int): Number of times to smooth the mesh
                  in [1, 1000], (optional)
               @xaxis (bool): Smooth along the X axis
                  (optional)
               @yaxis (bool): Smooth along the Y axis
                  (optional)
               @zaxis (bool): Smooth along the Z axis
                  (optional)

            '''

            pass

        def vertices_smooth_laplacian(repeat=1, lambda_factor=5e-05, lambda_border=5e-05, use_x=True, use_y=True, use_z=True, preserve_volume=True):
            '''Laplacian smooth of selected vertices
               Arguments:
               @repeat (int): in [1, 1000], (optional)
               @lambda_factor (float): in [1e-07, 1000], (optional)
               @lambda_border (float): in [1e-07, 1000], (optional)
               @use_x (bool): Smooth object along X axis
                  (optional)
               @use_y (bool): Smooth object along Y axis
                  (optional)
               @use_z (bool): Smooth object along Z axis
                  (optional)
               @preserve_volume (bool): Apply volume preservation after smooth
                  (optional)

            '''

            pass

        def wireframe(use_boundary=True, use_even_offset=True, use_relative_offset=False, use_replace=True, thickness=0.01, offset=0.01, use_crease=False, crease_weight=0.01):
            '''Create a solid wire-frame from faces
               Arguments:
               @use_boundary (bool): Inset face boundaries
                  (optional)
               @use_even_offset (bool): Scale the offset to give more even thickness
                  (optional)
               @use_relative_offset (bool): Scale the offset by surrounding geometry
                  (optional)
               @use_replace (bool): Remove original faces
                  (optional)
               @thickness (float): in [0, 10000], (optional)
               @offset (float): in [0, 10000], (optional)
               @use_crease (bool): Crease hub edges for improved subsurf
                  (optional)
               @crease_weight (float): in [0, 1000], (optional)

            '''

            pass

    class nla:
        '''Spcecial class, created just to reflect content of bpy.ops.nla'''

        def action_pushdown(channel_index=-1):
            '''Push action down onto the top of the NLA stack as a new strip
               Arguments:
               @channel_index (int): Index of NLA action channel to perform pushdown operation on
                  in [-1, inf], (optional)

            '''

            pass

        def action_sync_length(active=True):
            '''Synchronize the length of the referenced Action with the length used in the strip
               Arguments:
               @active (bool): Only sync the active length for the active strip
                  (optional)

            '''

            pass

        def action_unlink(force_delete=False):
            '''Unlink this action from the active action slot (and/or exit Tweak Mode)
               Arguments:
               @force_delete (bool): Clear Fake User and remove copy stashed in this datablock's NLA stack
                  (optional)

            '''

            pass

        def actionclip_add(action=''):
            '''Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track
               Arguments:
               @action (str): in [], (optional)

            '''

            pass

        def apply_scale():
            '''Apply scaling of selected strips to their referenced Actions
            '''

            pass

        def bake(frame_start=1, frame_end=250, step=1, only_selected=True, visual_keying=False, clear_constraints=False, clear_parents=False, use_current_action=False, bake_types={'POSE'}):
            '''Bake object/pose loc/scale/rotation animation to a new action
               Arguments:
               @frame_start (int): Start frame for baking
                  in [0, 300000], (optional)
               @frame_end (int): End frame for baking
                  in [1, 300000], (optional)
               @step (int): Frame Step
                  in [1, 120], (optional)
               @only_selected (bool): Only key selected object/bones
                  (optional)
               @visual_keying (bool): Keyframe from the final transformations (with constraints applied)
                  (optional)
               @clear_constraints (bool): Remove all constraints from keyed object/bones, and do 'visual' keying
                  (optional)
               @clear_parents (bool): Bake animation onto the object then clear parents (objects only)
                  (optional)
               @use_current_action (bool): Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature)
                  (optional)
               @bake_types (str): Which data's transformations to bake
                  set in {'POSE', 'OBJECT'}, (optional)

            '''

            pass

        def channels_click(extend=False):
            '''Handle clicks to select NLA channels
               Arguments:
               @extend (bool): (optional)

            '''

            pass

        def clear_scale():
            '''Reset scaling of selected strips
            '''

            pass

        def click_select(extend=False):
            '''Handle clicks to select NLA Strips
               Arguments:
               @extend (bool): (optional)

            '''

            pass

        def delete():
            '''Delete selected strips
            '''

            pass

        def duplicate(linked=False, mode='TRANSLATION'):
            '''Duplicate selected NLA-Strips, adding the new strips in new tracks above the originals
               Arguments:
               @linked (bool): When duplicating strips, assign new copies of the actions they use
                  (optional)
               @mode (str): in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)

            '''

            pass

        def fmodifier_add(type='NULL', only_active=True):
            '''Add F-Modifier to the active/selected NLA-Strips
               Arguments:
               @type (str): in ['NULL', 'GENERATOR', 'FNGENERATOR', 'ENVELOPE', 'CYCLES', 'NOISE', 'LIMITS', 'STEPPED'], (optional)
               @only_active (bool): Only add a F-Modifier of the specified type to the active strip
                  (optional)

            '''

            pass

        def fmodifier_copy():
            '''Copy the F-Modifier(s) of the active NLA-Strip
            '''

            pass

        def fmodifier_paste(only_active=True, replace=False):
            '''Add copied F-Modifiers to the selected NLA-Strips
               Arguments:
               @only_active (bool): Only paste F-Modifiers on active strip
                  (optional)
               @replace (bool): Replace existing F-Modifiers, instead of just appending to the end of the existing list
                  (optional)

            '''

            pass

        def make_single_user():
            '''Ensure that each action is only used once in the set of strips selected
            '''

            pass

        def meta_add():
            '''Add new meta-strips incorporating the selected strips
            '''

            pass

        def meta_remove():
            '''Separate out the strips held by the selected meta-strips
            '''

            pass

        def move_down():
            '''Move selected strips down a track if there's room
            '''

            pass

        def move_up():
            '''Move selected strips up a track if there's room
            '''

            pass

        def mute_toggle():
            '''Mute or un-mute selected strips
            '''

            pass

        def previewrange_set():
            '''Automatically set Preview Range based on range of keyframes
            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def select_all_toggle(invert=False):
            '''Select or deselect all NLA-Strips
               Arguments:
               @invert (bool): (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False):
            '''Use box selection to grab NLA-Strips
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @axis_range (bool): (optional)

            '''

            pass

        def select_leftright(mode='CHECK', extend=False):
            '''Select strips to the left or the right of the current frame
               Arguments:
               @mode (str): in ['CHECK', 'LEFT', 'RIGHT'], (optional)
               @extend (bool): (optional)

            '''

            pass

        def selected_objects_add():
            '''Make selected objects appear in NLA Editor by adding Animation Data
            '''

            pass

        def snap(type='CFRA'):
            '''Move start of strips to specified time
               Arguments:
               @type (str): in ['CFRA', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER'], (optional)

            '''

            pass

        def soundclip_add():
            '''Add a strip for controlling when speaker plays its sound clip
            '''

            pass

        def split():
            '''Split selected strips at their midpoints
            '''

            pass

        def swap():
            '''Swap order of selected strips within tracks
            '''

            pass

        def tracks_add(above_selected=False):
            '''Add NLA-Tracks above/after the selected tracks
               Arguments:
               @above_selected (bool): Add a new NLA Track above every existing selected one
                  (optional)

            '''

            pass

        def tracks_delete():
            '''Delete selected NLA-Tracks and the strips they contain
            '''

            pass

        def transition_add():
            '''Add a transition strip between two adjacent selected strips
            '''

            pass

        def tweakmode_enter(isolate_action=False):
            '''Enter tweaking mode for the action referenced by the active strip to edit its keyframes
               Arguments:
               @isolate_action (bool): Enable 'solo' on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack
                  (optional)

            '''

            pass

        def tweakmode_exit(isolate_action=False):
            '''Exit tweaking mode for the action referenced by the active strip
               Arguments:
               @isolate_action (bool): Disable 'solo' on any of the NLA Tracks after exiting tweak mode to get things back to normal
                  (optional)

            '''

            pass

        def view_all():
            '''Reset viewable area to show full strips range
            '''

            pass

        def view_frame():
            '''Reset viewable area to show range around current frame
            '''

            pass

        def view_selected():
            '''Reset viewable area to show selected strips range
            '''

            pass

    class node:
        '''Spcecial class, created just to reflect content of bpy.ops.node'''

        def add_and_link_node(type="", settings=None, use_transform=False, link_socket_index=0):
            '''Add a node to the active tree and link to an existing socket
               Arguments:
               @type (str): Node type
                  (optional, never None)
               @settings (NodeSetting): Settings to be applied on the newly created node
                  Collection of , (optional)
               @use_transform (bool): Start transform operator after inserting the node
                  (optional)
               @link_socket_index (int): Index of the socket to link
                  in [-inf, inf], (optional)

            '''

            pass

        def add_file(filepath="", filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', name="Image"):
            '''Add a file node to the current node editor
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @name (str): Datablock name to assign
                  (optional, never None)

            '''

            pass

        def add_mask(name="Mask"):
            '''Add a mask node to the current node editor
               Arguments:
               @name (str): Datablock name to assign
                  (optional, never None)

            '''

            pass

        def add_node(type="", settings=None, use_transform=False):
            '''Add a node to the active tree
               Arguments:
               @type (str): Node type
                  (optional, never None)
               @settings (NodeSetting): Settings to be applied on the newly created node
                  Collection of , (optional)
               @use_transform (bool): Start transform operator after inserting the node
                  (optional)

            '''

            pass

        def add_reroute(path=None, cursor=6):
            '''Add a reroute node
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @cursor (int): in [0, inf], (optional)

            '''

            pass

        def add_search(type="", settings=None, use_transform=False, node_item=''):
            '''Add a node to the active tree
               Arguments:
               @type (str): Node type
                  (optional, never None)
               @settings (NodeSetting): Settings to be applied on the newly created node
                  Collection of , (optional)
               @use_transform (bool): Start transform operator after inserting the node
                  (optional)
               @node_item (str): Node type
                  in [], (optional)

            '''

            pass

        def attach():
            '''Attach active node to a frame
            '''

            pass

        def backimage_fit():
            '''Fit the background image to the view
            '''

            pass

        def backimage_move():
            '''Move Node backdrop
            '''

            pass

        def backimage_sample():
            '''Use mouse to sample background image
            '''

            pass

        def backimage_zoom(factor=1.2):
            '''Zoom in/out the background image
               Arguments:
               @factor (float): in [0, 10], (optional)

            '''

            pass

        def clear_viewer_border():
            '''Clear the boundaries for viewer operations
            '''

            pass

        def clipboard_copy():
            '''Copies selected nodes to the clipboard
            '''

            pass

        def clipboard_paste():
            '''Pastes nodes from the clipboard to the active node tree
            '''

            pass

        def collapse_hide_unused_toggle():
            '''Toggle collapsed nodes and hide unused sockets
            '''

            pass

        def delete():
            '''Delete selected nodes
            '''

            pass

        def delete_reconnect():
            '''Delete nodes; will reconnect nodes as if deletion was muted
            '''

            pass

        def detach():
            '''Detach selected nodes from parents
            '''

            pass

        def detach_translate_attach(NODE_OT_detach=None, TRANSFORM_OT_translate=None, NODE_OT_attach=None):
            '''Detach nodes, move and attach to frame
               Arguments:
               @NODE_OT_detach (NODE_OT_detach): Detach selected nodes from parents
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)
               @NODE_OT_attach (NODE_OT_attach): Attach active node to a frame
                  (optional)

            '''

            pass

        def duplicate(keep_inputs=False):
            '''Duplicate selected nodes
               Arguments:
               @keep_inputs (bool): Keep the input links to duplicated nodes
                  (optional)

            '''

            pass

        def duplicate_move(NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
            '''Duplicate selected nodes and move them
               Arguments:
               @NODE_OT_duplicate (NODE_OT_duplicate): Duplicate selected nodes
                  (optional)
               @NODE_OT_translate_attach (NODE_OT_translate_attach): Move nodes and attach to frame
                  (optional)

            '''

            pass

        def duplicate_move_keep_inputs(NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
            '''Duplicate selected nodes keeping input links and move them
               Arguments:
               @NODE_OT_duplicate (NODE_OT_duplicate): Duplicate selected nodes
                  (optional)
               @NODE_OT_translate_attach (NODE_OT_translate_attach): Move nodes and attach to frame
                  (optional)

            '''

            pass

        def find_node(prev=False):
            '''Search for named node and allow to select and activate it
               Arguments:
               @prev (bool): (optional)

            '''

            pass

        def group_edit(exit=False):
            '''Edit node group
               Arguments:
               @exit (bool): (optional)

            '''

            pass

        def group_insert():
            '''Insert selected nodes into a node group
            '''

            pass

        def group_make():
            '''Make group from selected nodes
            '''

            pass

        def group_separate(type='COPY'):
            '''Separate selected nodes from the node group
               Arguments:
               @type (str): in ['COPY', 'MOVE'], (optional)

            '''

            pass

        def group_ungroup():
            '''Ungroup selected nodes
            '''

            pass

        def hide_socket_toggle():
            '''Toggle unused node socket display
            '''

            pass

        def hide_toggle():
            '''Toggle hiding of selected nodes
            '''

            pass

        def insert_offset():
            '''Automatically offset nodes on insertion
            '''

            pass

        def join():
            '''Attach selected nodes to a new common frame
            '''

            pass

        def link(detach=False):
            '''Use the mouse to create a link between two nodes
               Arguments:
               @detach (bool): Detach and redirect existing links
                  (optional)

            '''

            pass

        def link_make(replace=False):
            '''Makes a link between selected output in input sockets
               Arguments:
               @replace (bool): Replace socket connections with the new links
                  (optional)

            '''

            pass

        def link_viewer():
            '''Link to viewer node
            '''

            pass

        def links_cut(path=None, cursor=9):
            '''Use the mouse to cut (remove) some links
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @cursor (int): in [0, inf], (optional)

            '''

            pass

        def links_detach():
            '''Remove all links to selected nodes, and try to connect neighbor nodes together
            '''

            pass

        def move_detach_links(NODE_OT_links_detach=None, TRANSFORM_OT_translate=None, NODE_OT_insert_offset=None):
            '''Move a node to detach links
               Arguments:
               @NODE_OT_links_detach (NODE_OT_links_detach): Remove all links to selected nodes, and try to connect neighbor nodes together
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)
               @NODE_OT_insert_offset (NODE_OT_insert_offset): Automatically offset nodes on insertion
                  (optional)

            '''

            pass

        def move_detach_links_release(NODE_OT_links_detach=None, NODE_OT_translate_attach=None):
            '''Move a node to detach links
               Arguments:
               @NODE_OT_links_detach (NODE_OT_links_detach): Remove all links to selected nodes, and try to connect neighbor nodes together
                  (optional)
               @NODE_OT_translate_attach (NODE_OT_translate_attach): Move nodes and attach to frame
                  (optional)

            '''

            pass

        def mute_toggle():
            '''Toggle muting of the nodes
            '''

            pass

        def new_node_tree(type='', name="NodeTree"):
            '''Create a new node tree
               Arguments:
               @type (str): in [], (optional)
               @name (str): (optional, never None)

            '''

            pass

        def node_color_preset_add(name="", remove_active=False):
            '''Add or remove a Node Color Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def node_copy_color():
            '''Copy color to all selected nodes
            '''

            pass

        def options_toggle():
            '''Toggle option buttons display for selected nodes
            '''

            pass

        def output_file_add_socket(file_path="Image"):
            '''Add a new input to a file output node
               Arguments:
               @file_path (str): Sub-path of the output file
                  (optional, never None)

            '''

            pass

        def output_file_move_active_socket(direction='DOWN'):
            '''Move the active input of a file output node up or down the list
               Arguments:
               @direction (str): in ['UP', 'DOWN'], (optional)

            '''

            pass

        def output_file_remove_active_socket():
            '''Remove active input from a file output node
            '''

            pass

        def parent_set():
            '''Attach selected nodes
            '''

            pass

        def preview_toggle():
            '''Toggle preview display for selected nodes
            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def read_fullsamplelayers():
            '''Read all render layers of current scene, in full sample
            '''

            pass

        def read_renderlayers():
            '''Read all render layers of all used scenes
            '''

            pass

        def render_changed():
            '''Render current scene, when input node's layer has been changed
            '''

            pass

        def resize():
            '''Resize a node
            '''

            pass

        def select(mouse_x=0, mouse_y=0, extend=False):
            '''Select the node under the cursor
               Arguments:
               @mouse_x (int): in [-inf, inf], (optional)
               @mouse_y (int): in [-inf, inf], (optional)
               @extend (bool): (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''(De)select all nodes
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, tweak=False):
            '''Use box selection to select nodes
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @tweak (bool): Only activate when mouse is not over a node - useful for tweak gesture
                  (optional)

            '''

            pass

        def select_circle(x=0, y=0, radius=1, gesture_mode=0):
            '''Use circle selection to select nodes
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @radius (int): in [1, inf], (optional)
               @gesture_mode (int): in [-inf, inf], (optional)

            '''

            pass

        def select_grouped(extend=False, type='TYPE'):
            '''Select nodes with similar properties
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @type (str): in ['TYPE', 'COLOR', 'PREFIX', 'SUFFIX'], (optional)

            '''

            pass

        def select_lasso(path=None, deselect=False, extend=True):
            '''Select nodes using lasso selection
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @deselect (bool): Deselect rather than select items
                  (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_link_viewer(NODE_OT_select=None, NODE_OT_link_viewer=None):
            '''Select node and link it to a viewer node
               Arguments:
               @NODE_OT_select (NODE_OT_select): Select the node under the cursor
                  (optional)
               @NODE_OT_link_viewer (NODE_OT_link_viewer): Link to viewer node
                  (optional)

            '''

            pass

        def select_linked_from():
            '''Select nodes linked from the selected ones
            '''

            pass

        def select_linked_to():
            '''Select nodes linked to the selected ones
            '''

            pass

        def select_same_type_step(prev=False):
            '''Activate and view same node type, step by step
               Arguments:
               @prev (bool): (optional)

            '''

            pass

        def shader_script_update():
            '''Update shader script node with new sockets and options from the script
            '''

            pass

        def switch_view_update():
            '''Update views of selected node
            '''

            pass

        def toolbar():
            '''Toggles tool shelf display
            '''

            pass

        def translate_attach(TRANSFORM_OT_translate=None, NODE_OT_attach=None, NODE_OT_insert_offset=None):
            '''Move nodes and attach to frame
               Arguments:
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)
               @NODE_OT_attach (NODE_OT_attach): Attach active node to a frame
                  (optional)
               @NODE_OT_insert_offset (NODE_OT_insert_offset): Automatically offset nodes on insertion
                  (optional)

            '''

            pass

        def translate_attach_remove_on_cancel(TRANSFORM_OT_translate=None, NODE_OT_attach=None, NODE_OT_insert_offset=None):
            '''Move nodes and attach to frame
               Arguments:
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)
               @NODE_OT_attach (NODE_OT_attach): Attach active node to a frame
                  (optional)
               @NODE_OT_insert_offset (NODE_OT_insert_offset): Automatically offset nodes on insertion
                  (optional)

            '''

            pass

        def tree_path_parent():
            '''Go to parent node tree
            '''

            pass

        def tree_socket_add(in_out='IN'):
            '''Add an input or output socket to the current node tree
               Arguments:
               @in_out (str): in ['IN', 'OUT'], (optional)

            '''

            pass

        def tree_socket_move(direction='UP'):
            '''Move a socket up or down in the current node tree's sockets stack
               Arguments:
               @direction (str): in ['UP', 'DOWN'], (optional)

            '''

            pass

        def tree_socket_remove():
            '''Remove an input or output socket to the current node tree
            '''

            pass

        def view_all():
            '''Resize view so you can see all nodes
            '''

            pass

        def view_selected():
            '''Resize view so you can see selected nodes
            '''

            pass

        def viewer_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Set the boundaries for viewer operations
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

    class object:
        '''Spcecial class, created just to reflect content of bpy.ops.object'''

        def add(radius=1.0, type='EMPTY', view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add an object to the scene
               Arguments:
               @radius (float): in [0, inf], (optional)
               @type (str): in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'CAMERA', 'LAMP', 'SPEAKER'], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def add_named(linked=False, name=""):
            '''Add named object
               Arguments:
               @linked (bool): Duplicate object but not object data, linking to the original data
                  (optional)
               @name (str): Object name to add
                  (optional, never None)

            '''

            pass

        def align(bb_quality=True, align_mode='OPT_2', relative_to='OPT_4', align_axis={}):
            '''Align Objects
               Arguments:
               @bb_quality (bool): Enables high quality calculation of the bounding box for perfect results on complex shape meshes with rotation/scale (Slow)
                  (optional)
               @align_mode (str): Side of object to use for alignment
                  in ['OPT_1', 'OPT_2', 'OPT_3'], (optional)
               @relative_to (str): Reference location to align to
                  in ['OPT_1', 'OPT_2', 'OPT_3', 'OPT_4'], (optional)
               @align_axis (str): Align to axis
                  set in {'X', 'Y', 'Z'}, (optional)

            '''

            pass

        def anim_transforms_to_deltas():
            '''Convert object animation for normal transforms to delta transforms
            '''

            pass

        def armature_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add an armature object to the scene
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def bake(type='COMBINED', pass_filter={}, filepath="", width=512, height=512, margin=16, use_selected_to_active=False, cage_extrusion=0.0, cage_object="", normal_space='TANGENT', normal_r='POS_X', normal_g='POS_Y', normal_b='POS_Z', save_mode='INTERNAL', use_clear=False, use_cage=False, use_split_materials=False, use_automatic_name=False, uv_layer=""):
            '''Bake image textures of selected objects
               Arguments:
               @type (str): Type of pass to bake, some of them may not be supported by the current render engine
                  in ['COMBINED', 'AO', 'SHADOW', 'NORMAL', 'UV', 'EMIT', 'ENVIRONMENT', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'], (optional)
               @pass_filter (str): Filter to combined, diffuse, glossy, transmission and subsurface passes
                  set in {'NONE', 'AO', 'EMIT', 'DIRECT', 'INDIRECT', 'COLOR', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'}, (optional)
               @filepath (str): Image filepath to use when saving externally
                  (optional, never None)
               @width (int): Horizontal dimension of the baking map (external only)
                  in [1, inf], (optional)
               @height (int): Vertical dimension of the baking map (external only)
                  in [1, inf], (optional)
               @margin (int): Extends the baked result as a post process filter
                  in [0, inf], (optional)
               @use_selected_to_active (bool): Bake shading on the surface of selected objects to the active object
                  (optional)
               @cage_extrusion (float): Distance to use for the inward ray cast when using selected to active
                  in [0, inf], (optional)
               @cage_object (str): Object to use as cage, instead of calculating the cage from the active object with cage extrusion
                  (optional, never None)
               @normal_space (str): Choose normal space for baking
                  in ['OBJECT', 'TANGENT'], (optional)
               @normal_r (str): Axis to bake in red channel
                  in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional)
               @normal_g (str): Axis to bake in green channel
                  in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional)
               @normal_b (str): Axis to bake in blue channel
                  in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional)
               @save_mode (str): Choose how to save the baking map
                  in ['INTERNAL', 'EXTERNAL'], (optional)
               @use_clear (bool): Clear Images before baking (only for internal saving)
                  (optional)
               @use_cage (bool): Cast rays to active object from a cage
                  (optional)
               @use_split_materials (bool): Split baked maps per material, using material name in output file (external only)
                  (optional)
               @use_automatic_name (bool): Automatically name the output file with the pass type
                  (optional)
               @uv_layer (str): UV layer to override active
                  (optional, never None)

            '''

            pass

        def bake_image():
            '''Bake image textures of selected objects
            '''

            pass

        def camera_add(view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add a camera object to the scene
               Arguments:
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def constraint_add(type=''):
            '''Add a constraint to the active object
               Arguments:
               @type (str): in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'RIGID_BODY_JOINT', 'SHRINKWRAP'], (optional)

            '''

            pass

        def constraint_add_with_targets(type=''):
            '''Add a constraint to the active object, with target (where applicable) set to the selected Objects/Bones
               Arguments:
               @type (str): in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'RIGID_BODY_JOINT', 'SHRINKWRAP'], (optional)

            '''

            pass

        def constraints_clear():
            '''Clear all the constraints for the active Object only
            '''

            pass

        def constraints_copy():
            '''Copy constraints to other selected objects
            '''

            pass

        def convert(target='MESH', keep_original=False):
            '''Convert selected objects to another type
               Arguments:
               @target (str): Type of object to convert to
                  in ['CURVE', 'MESH'], (optional)
               @keep_original (bool): Keep original objects instead of replacing them
                  (optional)

            '''

            pass

        def correctivesmooth_bind(modifier=""):
            '''Bind base pose in Corrective Smooth modifier
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def data_transfer(use_reverse_transfer=False, use_freeze=False, data_type='', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1.0, ray_radius=0.0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1.0):
            '''Transfer data layer(s) (weights, edge sharp, ...) from active to selected meshes
               Arguments:
               @use_reverse_transfer (bool): Transfer from selected objects to active one
                  (optional)
               @use_freeze (bool): Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
                  (optional)
               @data_type (str): Which data to transfer
                  in ['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'VCOL', 'UV', 'SMOOTH', 'FREESTYLE_FACE'], (optional)
               @use_create (bool): Add data layers on destination meshes if needed
                  (optional)
               @vert_mapping (str): Method used to map source vertices to destination ones
                  in ['TOPOLOGY', 'NEAREST', 'EDGE_NEAREST', 'EDGEINTERP_NEAREST', 'POLY_NEAREST', 'POLYINTERP_NEAREST', 'POLYINTERP_VNORPROJ'], (optional)
               @edge_mapping (str): Method used to map source edges to destination ones
                  in ['TOPOLOGY', 'VERT_NEAREST', 'NEAREST', 'POLY_NEAREST', 'EDGEINTERP_VNORPROJ'], (optional)
               @loop_mapping (str): Method used to map source faces' corners to destination ones
                  in ['TOPOLOGY', 'NEAREST_NORMAL', 'NEAREST_POLYNOR', 'NEAREST_POLY', 'POLYINTERP_NEAREST', 'POLYINTERP_LNORPROJ'], (optional)
               @poly_mapping (str): Method used to map source faces to destination ones
                  in ['TOPOLOGY', 'NEAREST', 'NORMAL', 'POLYINTERP_PNORPROJ'], (optional)
               @use_auto_transform (bool): Automatically compute transformation to get the best possible match between source and destination meshes (WARNING: results will never be as good as manual matching of objects)
                  (optional)
               @use_object_transform (bool): Evaluate source and destination meshes in global space
                  (optional)
               @use_max_distance (bool): Source elements must be closer than given distance from destination one
                  (optional)
               @max_distance (float): Maximum allowed distance between source and destination element, for non-topology mappings
                  in [0, inf], (optional)
               @ray_radius (float): 'Width' of rays (especially useful when raycasting against vertices or edges)
                  in [0, inf], (optional)
               @islands_precision (float): Factor controlling precision of islands handling (the higher, the better the results)
                  in [0, 10], (optional)
               @layers_select_src (str): Which layers to transfer, in case of multi-layers types
                  in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], (optional)
               @layers_select_dst (str): How to match source and destination layers
                  in ['ACTIVE', 'NAME', 'INDEX'], (optional)
               @mix_mode (str): How to affect destination elements with source values
                  in ['REPLACE', 'ABOVE_THRESHOLD', 'BELOW_THRESHOLD', 'MIX', 'ADD', 'SUB', 'MUL'], (optional)
               @mix_factor (float): Factor to use when applying data to destination (exact behavior depends on mix mode)
                  in [0, 1], (optional)

            '''

            pass

        def datalayout_transfer(modifier="", data_type='', use_delete=False, layers_select_src='ACTIVE', layers_select_dst='ACTIVE'):
            '''Transfer layout of data layer(s) from active to selected meshes
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)
               @data_type (str): Which data to transfer
                  in ['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'VCOL', 'UV', 'SMOOTH', 'FREESTYLE_FACE'], (optional)
               @use_delete (bool): Also delete some data layers from destination if necessary, so that it matches exactly source
                  (optional)
               @layers_select_src (str): Which layers to transfer, in case of multi-layers types
                  in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], (optional)
               @layers_select_dst (str): How to match source and destination layers
                  in ['ACTIVE', 'NAME', 'INDEX'], (optional)

            '''

            pass

        def delete(use_global=False):
            '''Delete selected objects
               Arguments:
               @use_global (bool): Remove object from all scenes
                  (optional)

            '''

            pass

        def drop_named_image(filepath="", relative_path=True, name="", view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add an empty image type to scene with data
               Arguments:
               @filepath (str): Path to image file
                  (optional, never None)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @name (str): Image name to assign
                  (optional, never None)
               @view_align (bool): Align the new object to the view
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def drop_named_material(name="Material"):
            '''undocumented
               Arguments:
               @name (str): Material name to assign
                  (optional, never None)

            '''

            pass

        def dupli_offset_from_cursor():
            '''Set offset used for DupliGroup based on cursor position
            '''

            pass

        def duplicate(linked=False, mode='TRANSLATION'):
            '''Duplicate selected objects
               Arguments:
               @linked (bool): Duplicate object but not object data, linking to the original data
                  (optional)
               @mode (str): in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)

            '''

            pass

        def duplicate_move(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
            '''Duplicate selected objects and move them
               Arguments:
               @OBJECT_OT_duplicate (OBJECT_OT_duplicate): Duplicate selected objects
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def duplicate_move_linked(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
            '''Duplicate selected objects and move them
               Arguments:
               @OBJECT_OT_duplicate (OBJECT_OT_duplicate): Duplicate selected objects
                  (optional)
               @TRANSFORM_OT_translate (TRANSFORM_OT_translate): Translate (move) selected items
                  (optional)

            '''

            pass

        def duplicates_make_real(use_base_parent=False, use_hierarchy=False):
            '''Make dupli objects attached to this object real
               Arguments:
               @use_base_parent (bool): Parent newly created objects to the original duplicator
                  (optional)
               @use_hierarchy (bool): Maintain parent child relationships
                  (optional)

            '''

            pass

        def editmode_toggle():
            '''Toggle object's editmode
            '''

            pass

        def effector_add(type='FORCE', radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add an empty object with a physics effector to the scene
               Arguments:
               @type (str): in ['FORCE', 'WIND', 'VORTEX', 'MAGNET', 'HARMONIC', 'CHARGE', 'LENNARDJ', 'TEXTURE', 'GUIDE', 'BOID', 'TURBULENCE', 'DRAG', 'SMOKE'], (optional)
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def empty_add(type='PLAIN_AXES', radius=1.0, view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add an empty object to the scene
               Arguments:
               @type (str): in ['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE', 'IMAGE'], (optional)
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def explode_refresh(modifier=""):
            '''Refresh data in the Explode modifier
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def forcefield_toggle():
            '''Toggle object's force field
            '''

            pass

        def game_physics_copy():
            '''Copy game physics properties to other selected objects
            '''

            pass

        def game_property_clear():
            '''Remove all game properties from all selected objects
            '''

            pass

        def game_property_copy(operation='COPY', property=''):
            '''Copy/merge/replace a game property from active object to all selected objects
               Arguments:
               @operation (str): in ['REPLACE', 'MERGE', 'COPY'], (optional)
               @property (str): Properties to copy
                  in [], (optional)

            '''

            pass

        def game_property_move(index=0, direction='UP'):
            '''Move game property
               Arguments:
               @index (int): Property index to move
                  in [0, inf], (optional)
               @direction (str): Direction for moving the property
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def game_property_new(type='FLOAT', name=""):
            '''Create a new property available to the game engine
               Arguments:
               @type (str): Type of game property to add
                  in ['BOOL', 'INT', 'FLOAT', 'STRING', 'TIMER'], (optional)
               @name (str): Name of the game property to add
                  (optional, never None)

            '''

            pass

        def game_property_remove(index=0):
            '''Remove game property
               Arguments:
               @index (int): Property index to remove
                  in [0, inf], (optional)

            '''

            pass

        def group_add():
            '''Add an object to a new group
            '''

            pass

        def group_instance_add(name="Group", group='', view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add a dupligroup instance
               Arguments:
               @name (str): Group name to add
                  (optional, never None)
               @group (str): in [], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def group_link(group=''):
            '''Add an object to an existing group
               Arguments:
               @group (str): in [], (optional)

            '''

            pass

        def group_remove():
            '''Remove the active object from this group
            '''

            pass

        def group_unlink():
            '''Unlink the group from all objects
            '''

            pass

        def grouped_select():
            '''Select all objects in group
            '''

            pass

        def hide_render_clear():
            '''Reveal the render object by setting the hide render flag
            '''

            pass

        def hide_render_clear_all():
            '''Reveal all render objects by setting the hide render flag
            '''

            pass

        def hide_render_set(unselected=False):
            '''Hide the render object by setting the hide render flag
               Arguments:
               @unselected (bool): Hide unselected rather than selected objects
                  (optional)

            '''

            pass

        def hide_view_clear():
            '''Reveal the object by setting the hide flag
            '''

            pass

        def hide_view_set(unselected=False):
            '''Hide the object by setting the hide flag
               Arguments:
               @unselected (bool): Hide unselected rather than selected objects
                  (optional)

            '''

            pass

        def hook_add_newob():
            '''Hook selected vertices to a newly created object
            '''

            pass

        def hook_add_selob(use_bone=False):
            '''Hook selected vertices to the first selected object
               Arguments:
               @use_bone (bool): Assign the hook to the hook objects active bone
                  (optional)

            '''

            pass

        def hook_assign(modifier=''):
            '''Assign the selected vertices to a hook
               Arguments:
               @modifier (str): Modifier number to assign to
                  in [], (optional)

            '''

            pass

        def hook_recenter(modifier=''):
            '''Set hook center to cursor position
               Arguments:
               @modifier (str): Modifier number to assign to
                  in [], (optional)

            '''

            pass

        def hook_remove(modifier=''):
            '''Remove a hook from the active object
               Arguments:
               @modifier (str): Modifier number to remove
                  in [], (optional)

            '''

            pass

        def hook_reset(modifier=''):
            '''Recalculate and clear offset transformation
               Arguments:
               @modifier (str): Modifier number to assign to
                  in [], (optional)

            '''

            pass

        def hook_select(modifier=''):
            '''Select affected vertices on mesh
               Arguments:
               @modifier (str): Modifier number to remove
                  in [], (optional)

            '''

            pass

        def isolate_type_render():
            '''Hide unselected render objects of same type as active by setting the hide render flag
            '''

            pass

        def join():
            '''Join selected objects into active object
            '''

            pass

        def join_shapes():
            '''Merge selected objects to shapes of active object
            '''

            pass

        def join_uvs():
            '''Transfer UV Maps from active to selected objects (needs matching geometry)
            '''

            pass

        def lamp_add(type='POINT', radius=1.0, view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add a lamp object to the scene
               Arguments:
               @type (str): in ['POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'], (optional)
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def laplaciandeform_bind(modifier=""):
            '''Bind mesh to system in laplacian deform modifier
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def location_clear(clear_delta=False):
            '''Clear the object's location
               Arguments:
               @clear_delta (bool): Clear delta location in addition to clearing the normal location transform
                  (optional)

            '''

            pass

        def lod_add():
            '''Add a level of detail to this object
            '''

            pass

        def lod_by_name():
            '''Add levels of detail to this object based on object names
            '''

            pass

        def lod_clear_all():
            '''Remove all levels of detail from this object
            '''

            pass

        def lod_generate(count=3, target=0.1, package=False):
            '''Generate levels of detail using the decimate modifier
               Arguments:
               @count (int): in [-inf, inf], (optional)
               @target (float): in [0, 1], (optional)
               @package (bool): (optional)

            '''

            pass

        def lod_remove(index=1):
            '''Remove a level of detail from this object
               Arguments:
               @index (int): in [1, inf], (optional)

            '''

            pass

        def logic_bricks_copy():
            '''Copy logic bricks to other selected objects
            '''

            pass

        def make_dupli_face():
            '''Convert objects into dupli-face instanced
            '''

            pass

        def make_links_data(type='OBDATA'):
            '''Apply active object links to other selected objects
               Arguments:
               @type (str): in ['OBDATA', 'MATERIAL', 'ANIMATION', 'GROUPS', 'DUPLIGROUP', 'MODIFIERS', 'FONTS'], (optional)

            '''

            pass

        def make_links_scene(scene=''):
            '''Link selection to another scene
               Arguments:
               @scene (str): in [], (optional)

            '''

            pass

        def make_local(type='SELECT_OBJECT'):
            '''Make library linked datablocks local to this file
               Arguments:
               @type (str): in ['SELECT_OBJECT', 'SELECT_OBDATA', 'SELECT_OBDATA_MATERIAL', 'ALL'], (optional)

            '''

            pass

        def make_single_user(type='SELECTED_OBJECTS', object=False, obdata=False, material=False, texture=False, animation=False):
            '''Make linked data local to each object
               Arguments:
               @type (str): in ['SELECTED_OBJECTS', 'ALL'], (optional)
               @object (bool): Make single user objects
                  (optional)
               @obdata (bool): Make single user object data
                  (optional)
               @material (bool): Make materials local to each datablock
                  (optional)
               @texture (bool): Make textures local to each material (needs 'Materials' to be set too)
                  (optional)
               @animation (bool): Make animation data local to each object
                  (optional)

            '''

            pass

        def material_slot_add():
            '''Add a new material slot
            '''

            pass

        def material_slot_assign():
            '''Assign active material slot to selection
            '''

            pass

        def material_slot_copy():
            '''Copies materials to other selected objects
            '''

            pass

        def material_slot_deselect():
            '''Deselect by active material slot
            '''

            pass

        def material_slot_move(direction='UP'):
            '''Move the active material up/down in the list
               Arguments:
               @direction (str): Direction to move, UP or DOWN
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def material_slot_remove():
            '''Remove the selected material slot
            '''

            pass

        def material_slot_select():
            '''Select by active material slot
            '''

            pass

        def meshdeform_bind(modifier=""):
            '''Bind mesh to cage in mesh deform modifier
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def metaball_add(type='BALL', radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add an metaball object to the scene
               Arguments:
               @type (str): in ['BALL', 'CAPSULE', 'PLANE', 'ELLIPSOID', 'CUBE'], (optional)
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def mode_set(mode='OBJECT', toggle=False):
            '''Sets the object interaction mode
               Arguments:
               @mode (str): in ['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'GPENCIL_EDIT'], (optional)
               @toggle (bool): (optional)

            '''

            pass

        def modifier_add(type='SUBSURF'):
            '''Add a modifier to the active object
               Arguments:
               @type (str): in ['DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'MASK', 'MIRROR', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'WIREFRAME', 'ARMATURE', 'CAST', 'CORRECTIVE_SMOOTH', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANSMOOTH', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'WARP', 'WAVE', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID_SIMULATION', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SMOKE', 'SOFT_BODY', 'SURFACE'], (optional)

            '''

            pass

        def modifier_apply(apply_as='DATA', modifier=""):
            '''Apply modifier and remove from the stack
               Arguments:
               @apply_as (str): How to apply the modifier to the geometry
                  in ['DATA', 'SHAPE'], (optional)
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def modifier_convert(modifier=""):
            '''Convert particles to a mesh object
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def modifier_copy(modifier=""):
            '''Duplicate modifier at the same position in the stack
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def modifier_move_down(modifier=""):
            '''Move modifier down in the stack
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def modifier_move_up(modifier=""):
            '''Move modifier up in the stack
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def modifier_remove(modifier=""):
            '''Remove a modifier from the active object
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def move_to_layer(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Move the object to different layers
               Arguments:
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def multires_base_apply(modifier=""):
            '''Modify the base mesh to conform to the displaced mesh
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def multires_external_pack():
            '''Pack displacements from an external file
            '''

            pass

        def multires_external_save(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=True, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', modifier=""):
            '''Save displacements to an external file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def multires_higher_levels_delete(modifier=""):
            '''Deletes the higher resolution mesh, potential loss of detail
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def multires_reshape(modifier=""):
            '''Copy vertex coordinates from other object
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def multires_subdivide(modifier=""):
            '''Add a new level of subdivision
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def ocean_bake(modifier="", free=False):
            '''Bake an image sequence of ocean data
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)
               @free (bool): Free the bake, rather than generating it
                  (optional)

            '''

            pass

        def origin_clear():
            '''Clear the object's origin
            '''

            pass

        def origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN'):
            '''Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor
               Arguments:
               @type (str): in ['GEOMETRY_ORIGIN', 'ORIGIN_GEOMETRY', 'ORIGIN_CURSOR', 'ORIGIN_CENTER_OF_MASS'], (optional)
               @center (str): in ['MEDIAN', 'BOUNDS'], (optional)

            '''

            pass

        def parent_clear(type='CLEAR'):
            '''Clear the object's parenting
               Arguments:
               @type (str): in ['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE'], (optional)

            '''

            pass

        def parent_no_inverse_set():
            '''Set the object's parenting without setting the inverse parent correction
            '''

            pass

        def parent_set(type='OBJECT', xmirror=False, keep_transform=False):
            '''Set the object's parenting
               Arguments:
               @type (str): in ['OBJECT', 'ARMATURE', 'ARMATURE_NAME', 'ARMATURE_AUTO', 'ARMATURE_ENVELOPE', 'BONE', 'BONE_RELATIVE', 'CURVE', 'FOLLOW', 'PATH_CONST', 'LATTICE', 'VERTEX', 'VERTEX_TRI'], (optional)
               @xmirror (bool): Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
                  (optional)
               @keep_transform (bool): Apply transformation before parenting
                  (optional)

            '''

            pass

        def particle_system_add():
            '''Add a particle system
            '''

            pass

        def particle_system_remove():
            '''Remove the selected particle system
            '''

            pass

        def paths_calculate(start_frame=1, end_frame=250):
            '''Calculate motion paths for the selected objects
               Arguments:
               @start_frame (int): First frame to calculate object paths on
                  in [-500000, 500000], (optional)
               @end_frame (int): Last frame to calculate object paths on
                  in [-500000, 500000], (optional)

            '''

            pass

        def paths_clear(only_selected=False):
            '''Clear path caches for all objects, hold Shift key for selected objects only
               Arguments:
               @only_selected (bool): Only clear paths from selected objects
                  (optional)

            '''

            pass

        def paths_update():
            '''Recalculate paths for selected objects
            '''

            pass

        def posemode_toggle():
            '''Enable or disable posing/selecting bones
            '''

            pass

        def proxy_make(object='DEFAULT'):
            '''Add empty object to become local replacement data of a library-linked object
               Arguments:
               @object (str): Name of lib-linked/grouped object to make a proxy for
                  in ['DEFAULT'], (optional)

            '''

            pass

        def quick_explode(style='EXPLODE', amount=100, frame_duration=50, frame_start=1, frame_end=10, velocity=1.0, fade=True):
            '''undocumented
               Arguments:
               @style (str): in ['EXPLODE', 'BLEND'], (optional)
               @amount (int): in [2, 10000], (optional)
               @frame_duration (int): in [1, 300000], (optional)
               @frame_start (int): in [1, 300000], (optional)
               @frame_end (int): in [1, 300000], (optional)
               @velocity (float): in [0, 300000], (optional)
               @fade (bool): Fade the pieces over time
                  (optional)

            '''

            pass

        def quick_fluid(style='BASIC', initial_velocity=(0.0, 0.0, 0.0), show_flows=False, start_baking=False):
            '''undocumented
               Arguments:
               @style (str): in ['INFLOW', 'BASIC'], (optional)
               @initial_velocity (float): Initial velocity of the fluid
                  array of 3 items in [-100, 100], (optional)
               @show_flows (bool): Keep the fluid objects visible during rendering
                  (optional)
               @start_baking (bool): Start baking the fluid immediately after creating the domain object
                  (optional)

            '''

            pass

        def quick_fur(density='MEDIUM', view_percentage=10, length=0.1):
            '''undocumented
               Arguments:
               @density (str): in ['LIGHT', 'MEDIUM', 'HEAVY'], (optional)
               @view_percentage (int): in [1, 100], (optional)
               @length (float): in [0.001, 100], (optional)

            '''

            pass

        def quick_smoke(style='SMOKE', show_flows=False):
            '''undocumented
               Arguments:
               @style (str): in ['SMOKE', 'FIRE', 'BOTH'], (optional)
               @show_flows (bool): Keep the smoke objects visible during rendering
                  (optional)

            '''

            pass

        def randomize_transform(random_seed=0, use_delta=False, use_loc=True, loc=(0.0, 0.0, 0.0), use_rot=True, rot=(0.0, 0.0, 0.0), use_scale=True, scale_even=False, scale=(1.0, 1.0, 1.0)):
            '''Randomize objects loc/rot/scale
               Arguments:
               @random_seed (int): Seed value for the random generator
                  in [0, 10000], (optional)
               @use_delta (bool): Randomize delta transform values instead of regular transform
                  (optional)
               @use_loc (bool): Randomize the location values
                  (optional)
               @loc (float): Maximum distance the objects can spread over each axis
                  array of 3 items in [-100, 100], (optional)
               @use_rot (bool): Randomize the rotation values
                  (optional)
               @rot (float): Maximum rotation over each axis
                  array of 3 items in [-3.14159, 3.14159], (optional)
               @use_scale (bool): Randomize the scale values
                  (optional)
               @scale_even (bool): Use the same scale value for all axis
                  (optional)
               @scale (float): Maximum scale randomization over each axis
                  array of 3 items in [-100, 100], (optional)

            '''

            pass

        def rotation_clear(clear_delta=False):
            '''Clear the object's rotation
               Arguments:
               @clear_delta (bool): Clear delta rotation in addition to clearing the normal rotation transform
                  (optional)

            '''

            pass

        def scale_clear(clear_delta=False):
            '''Clear the object's scale
               Arguments:
               @clear_delta (bool): Clear delta scale in addition to clearing the normal scale transform
                  (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''Change selection of all visible objects in scene
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_by_layer(match='EXACT', extend=False, layers=1):
            '''Select all visible objects on a layer
               Arguments:
               @match (str): in ['EXACT', 'SHARED'], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @layers (int): in [1, 20], (optional)

            '''

            pass

        def select_by_type(extend=False, type='MESH'):
            '''Select all visible objects that are of a type
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @type (str): in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'CAMERA', 'LAMP', 'SPEAKER'], (optional)

            '''

            pass

        def select_camera(extend=False):
            '''Select the active camera
               Arguments:
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_grouped(extend=False, type='CHILDREN_RECURSIVE'):
            '''Select all visible objects grouped by various properties
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @type (str): in ['CHILDREN_RECURSIVE', 'CHILDREN', 'PARENT', 'SIBLINGS', 'TYPE', 'LAYER', 'GROUP', 'HOOK', 'PASS', 'COLOR', 'PROPERTIES', 'KEYINGSET', 'LAMP_TYPE'], (optional)

            '''

            pass

        def select_hierarchy(direction='PARENT', extend=False):
            '''Select object relative to the active object's position in the hierarchy
               Arguments:
               @direction (str): Direction to select in the hierarchy
                  in ['PARENT', 'CHILD'], (optional)
               @extend (bool): Extend the existing selection
                  (optional)

            '''

            pass

        def select_less():
            '''Deselect objects at the boundaries of parent/child relationships
            '''

            pass

        def select_linked(extend=False, type='OBDATA'):
            '''Select all visible objects that are linked
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @type (str): in ['OBDATA', 'MATERIAL', 'TEXTURE', 'DUPGROUP', 'PARTICLE', 'LIBRARY', 'LIBRARY_OBDATA'], (optional)

            '''

            pass

        def select_mirror(extend=False):
            '''Select the Mirror objects of the selected object eg. L.sword -> R.sword
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_more():
            '''Select connected parent/child objects
            '''

            pass

        def select_pattern(pattern="*", case_sensitive=False, extend=True):
            '''Select objects matching a naming pattern
               Arguments:
               @pattern (str): Name filter using '*', '?' and '[abc]' unix style wildcards
                  (optional, never None)
               @case_sensitive (bool): Do a case sensitive compare
                  (optional)
               @extend (bool): Extend the existing selection
                  (optional)

            '''

            pass

        def select_random(percent=50.0, seed=0, action='SELECT'):
            '''Set select on random visible objects
               Arguments:
               @percent (float): Percentage of objects to select randomly
                  in [0, 100], (optional)
               @seed (int): Seed for the random number generator
                  in [0, inf], (optional)
               @action (str): Selection action to execute
                  in ['SELECT', 'DESELECT'], (optional)

            '''

            pass

        def select_same_group(group=""):
            '''Select object in the same group
               Arguments:
               @group (str): Name of the group to select
                  (optional, never None)

            '''

            pass

        def shade_flat():
            '''Render and display faces uniform, using Face Normals
            '''

            pass

        def shade_smooth():
            '''Render and display faces smooth, using interpolated Vertex Normals
            '''

            pass

        def shape_key_add(from_mix=True):
            '''Add shape key to the object
               Arguments:
               @from_mix (bool): Create the new shape key from the existing mix of keys
                  (optional)

            '''

            pass

        def shape_key_clear():
            '''Clear weights for all shape keys
            '''

            pass

        def shape_key_mirror(use_topology=False):
            '''Mirror the current shape key along the local X axis
               Arguments:
               @use_topology (bool): Use topology based mirroring (for when both sides of mesh have matching, unique topology)
                  (optional)

            '''

            pass

        def shape_key_move(type='TOP'):
            '''Move the active shape key up/down in the list
               Arguments:
               @type (str): in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional)

            '''

            pass

        def shape_key_remove(all=False):
            '''Remove shape key from the object
               Arguments:
               @all (bool): Remove all shape keys
                  (optional)

            '''

            pass

        def shape_key_retime():
            '''Resets the timing for absolute shape keys
            '''

            pass

        def shape_key_transfer(mode='OFFSET', use_clamp=False):
            '''Copy another selected objects active shape to this one by applying the relative offsets
               Arguments:
               @mode (str): Relative shape positions to the new shape method
                  in ['OFFSET', 'RELATIVE_FACE', 'RELATIVE_EDGE'], (optional)
               @use_clamp (bool): Clamp the transformation to the distance each vertex moves in the original shape
                  (optional)

            '''

            pass

        def skin_armature_create(modifier=""):
            '''Create an armature that parallels the skin layout
               Arguments:
               @modifier (str): Name of the modifier to edit
                  (optional, never None)

            '''

            pass

        def skin_loose_mark_clear(action='MARK'):
            '''Mark/clear selected vertices as loose
               Arguments:
               @action (str): in ['MARK', 'CLEAR'], (optional)

            '''

            pass

        def skin_radii_equalize():
            '''Make skin radii of selected vertices equal on each axis
            '''

            pass

        def skin_root_mark():
            '''Mark selected vertices as roots
            '''

            pass

        def slow_parent_clear():
            '''Clear the object's slow parent
            '''

            pass

        def slow_parent_set():
            '''Set the object's slow parent
            '''

            pass

        def speaker_add(view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add a speaker object to the scene
               Arguments:
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def subdivision_set(level=1, relative=False):
            '''Sets a Subdivision Surface Level (1-5)
               Arguments:
               @level (int): in [-100, 100], (optional)
               @relative (bool): Apply the subsurf level as an offset relative to the current level
                  (optional)

            '''

            pass

        def text_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Add a text object to the scene
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def track_clear(type='CLEAR'):
            '''Clear tracking constraint or flag from object
               Arguments:
               @type (str): in ['CLEAR', 'CLEAR_KEEP_TRANSFORM'], (optional)

            '''

            pass

        def track_set(type='DAMPTRACK'):
            '''Make the object track another object, using various methods/constraints
               Arguments:
               @type (str): in ['DAMPTRACK', 'TRACKTO', 'LOCKTRACK'], (optional)

            '''

            pass

        def transform_apply(location=False, rotation=False, scale=False):
            '''Apply the object's transformation to its data
               Arguments:
               @location (bool): (optional)
               @rotation (bool): (optional)
               @scale (bool): (optional)

            '''

            pass

        def transforms_to_deltas(mode='ALL', reset_values=True):
            '''Convert normal object transforms to delta transforms, any existing delta transforms will be included as well
               Arguments:
               @mode (str): Which transforms to transfer
                  in ['ALL', 'LOC', 'ROT', 'SCALE'], (optional)
               @reset_values (bool): Clear transform values after transferring to deltas
                  (optional)

            '''

            pass

        def unlink_data():
            '''undocumented
            '''

            pass

        def vertex_group_add():
            '''Add a new vertex group to the active object
            '''

            pass

        def vertex_group_assign():
            '''Assign the selected vertices to the active vertex group
            '''

            pass

        def vertex_group_assign_new():
            '''Assign the selected vertices to a new vertex group
            '''

            pass

        def vertex_group_clean(group_select_mode='', limit=0.0, keep_single=False):
            '''Remove vertex group assignments which are not required
               Arguments:
               @group_select_mode (str): Define which subset of Groups shall be used
                  in [], (optional)
               @limit (float): Remove vertices which weight is below or equal to this limit
                  in [0, 1], (optional)
               @keep_single (bool): Keep verts assigned to at least one group when cleaning
                  (optional)

            '''

            pass

        def vertex_group_copy():
            '''Make a copy of the active vertex group
            '''

            pass

        def vertex_group_copy_to_linked():
            '''Replace vertex groups of all users of the same geometry data by vertex groups of active object
            '''

            pass

        def vertex_group_copy_to_selected():
            '''Replace vertex groups of selected objects by vertex groups of active object
            '''

            pass

        def vertex_group_deselect():
            '''Deselect all selected vertices assigned to the active vertex group
            '''

            pass

        def vertex_group_fix(dist=0.0, strength=1.0, accuracy=1.0):
            '''Modify the position of selected vertices by changing only their respective groups' weights (this tool may be slow for many vertices)
               Arguments:
               @dist (float): The distance to move to
                  in [-inf, inf], (optional)
               @strength (float): The distance moved can be changed by this multiplier
                  in [-2, inf], (optional)
               @accuracy (float): Change the amount weights are altered with each iteration: lower values are slower
                  in [0.05, inf], (optional)

            '''

            pass

        def vertex_group_invert(group_select_mode='', auto_assign=True, auto_remove=True):
            '''Invert active vertex group's weights
               Arguments:
               @group_select_mode (str): Define which subset of Groups shall be used
                  in [], (optional)
               @auto_assign (bool): Add verts from groups that have zero weight before inverting
                  (optional)
               @auto_remove (bool): Remove verts from groups that have zero weight after inverting
                  (optional)

            '''

            pass

        def vertex_group_levels(group_select_mode='', offset=0.0, gain=1.0):
            '''Add some offset and multiply with some gain the weights of the active vertex group
               Arguments:
               @group_select_mode (str): Define which subset of Groups shall be used
                  in [], (optional)
               @offset (float): Value to add to weights
                  in [-1, 1], (optional)
               @gain (float): Value to multiply weights by
                  in [0, inf], (optional)

            '''

            pass

        def vertex_group_limit_total(group_select_mode='', limit=4):
            '''Limit deform weights associated with a vertex to a specified number by removing lowest weights
               Arguments:
               @group_select_mode (str): Define which subset of Groups shall be used
                  in [], (optional)
               @limit (int): Maximum number of deform weights
                  in [1, 32], (optional)

            '''

            pass

        def vertex_group_lock(action='TOGGLE'):
            '''Change the lock state of all vertex groups of active object
               Arguments:
               @action (str): Lock action to execute on vertex groups
                  in ['TOGGLE', 'LOCK', 'UNLOCK', 'INVERT'], (optional)

            '''

            pass

        def vertex_group_mirror(mirror_weights=True, flip_group_names=True, all_groups=False, use_topology=False):
            '''Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected
               Arguments:
               @mirror_weights (bool): Mirror weights
                  (optional)
               @flip_group_names (bool): Flip vertex group names
                  (optional)
               @all_groups (bool): Mirror all vertex groups weights
                  (optional)
               @use_topology (bool): Use topology based mirroring (for when both sides of mesh have matching, unique topology)
                  (optional)

            '''

            pass

        def vertex_group_move(direction='UP'):
            '''Move the active vertex group up/down in the list
               Arguments:
               @direction (str): Direction to move, UP or DOWN
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def vertex_group_normalize():
            '''Normalize weights of the active vertex group, so that the highest ones are now 1.0
            '''

            pass

        def vertex_group_normalize_all(group_select_mode='', lock_active=True):
            '''Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0
               Arguments:
               @group_select_mode (str): Define which subset of Groups shall be used
                  in [], (optional)
               @lock_active (bool): Keep the values of the active group while normalizing others
                  (optional)

            '''

            pass

        def vertex_group_quantize(group_select_mode='', steps=4):
            '''Set weights to a fixed number of steps
               Arguments:
               @group_select_mode (str): Define which subset of Groups shall be used
                  in [], (optional)
               @steps (int): Number of steps between 0 and 1
                  in [1, 1000], (optional)

            '''

            pass

        def vertex_group_remove(all=False):
            '''Delete the active or all vertex groups from the active object
               Arguments:
               @all (bool): Remove all vertex groups
                  (optional)

            '''

            pass

        def vertex_group_remove_from(use_all_groups=False, use_all_verts=False):
            '''Remove the selected vertices from active or all vertex group(s)
               Arguments:
               @use_all_groups (bool): Remove from all groups
                  (optional)
               @use_all_verts (bool): Clear the active group
                  (optional)

            '''

            pass

        def vertex_group_select():
            '''Select all the vertices assigned to the active vertex group
            '''

            pass

        def vertex_group_set_active(group=''):
            '''Set the active vertex group
               Arguments:
               @group (str): Vertex group to set as active
                  in [], (optional)

            '''

            pass

        def vertex_group_smooth(group_select_mode='', factor=0.5, repeat=1, expand=0.0, source='ALL'):
            '''Smooth weights for selected vertices
               Arguments:
               @group_select_mode (str): Define which subset of Groups shall be used
                  in [], (optional)
               @factor (float): in [0, 1], (optional)
               @repeat (int): in [1, 10000], (optional)
               @expand (float): Expand/contract weights
                  in [-1, 1], (optional)
               @source (str): Vertices to mix with
                  in ['ALL', 'SELECT', 'DESELECT'], (optional)

            '''

            pass

        def vertex_group_sort(sort_type='NAME'):
            '''Sort vertex groups
               Arguments:
               @sort_type (str): Sort type
                  in ['NAME', 'BONE_HIERARCHY'], (optional)

            '''

            pass

        def vertex_parent_set():
            '''Parent selected objects to the selected vertices
            '''

            pass

        def vertex_weight_copy():
            '''Copy weights from active to selected
            '''

            pass

        def vertex_weight_delete(weight_group=-1):
            '''Delete this weight from the vertex (disabled if vertex group is locked)
               Arguments:
               @weight_group (int): Index of source weight in active vertex group
                  in [-1, inf], (optional)

            '''

            pass

        def vertex_weight_normalize_active_vertex():
            '''Normalize active vertex's weights
            '''

            pass

        def vertex_weight_paste(weight_group=-1):
            '''Copy this group's weight to other selected verts (disabled if vertex group is locked)
               Arguments:
               @weight_group (int): Index of source weight in active vertex group
                  in [-1, inf], (optional)

            '''

            pass

        def vertex_weight_set_active(weight_group=-1):
            '''Set as active vertex group
               Arguments:
               @weight_group (int): Index of source weight in active vertex group
                  in [-1, inf], (optional)

            '''

            pass

        def visual_transform_apply():
            '''Apply the object's visual transformation to its data
            '''

            pass

    class outliner:
        '''Spcecial class, created just to reflect content of bpy.ops.outliner'''

        def action_set(action=''):
            '''Change the active action used
               Arguments:
               @action (str): in [], (optional)

            '''

            pass

        def animdata_operation(type='CLEAR_ANIMDATA'):
            '''undocumented
               Arguments:
               @type (str): in ['CLEAR_ANIMDATA', 'SET_ACT', 'CLEAR_ACT', 'REFRESH_DRIVERS', 'CLEAR_DRIVERS'], (optional)

            '''

            pass

        def constraint_operation(type='ENABLE'):
            '''undocumented
               Arguments:
               @type (str): in ['ENABLE', 'DISABLE', 'DELETE'], (optional)

            '''

            pass

        def data_operation(type='SELECT'):
            '''undocumented
               Arguments:
               @type (str): in ['SELECT', 'DESELECT', 'HIDE', 'UNHIDE', 'SELECT_LINKED'], (optional)

            '''

            pass

        def drivers_add_selected():
            '''Add drivers to selected items
            '''

            pass

        def drivers_delete_selected():
            '''Delete drivers assigned to selected items
            '''

            pass

        def expanded_toggle():
            '''Expand/Collapse all items
            '''

            pass

        def group_link(object="Object"):
            '''Link Object to Group in Outliner
               Arguments:
               @object (str): Target Object
                  (optional, never None)

            '''

            pass

        def group_operation(type='UNLINK'):
            '''undocumented
               Arguments:
               @type (str): in ['UNLINK', 'LOCAL', 'LINK', 'DELETE', 'REMAP', 'INSTANCE', 'TOGVIS', 'TOGSEL', 'TOGREN', 'RENAME'], (optional)

            '''

            pass

        def id_delete():
            '''Delete the ID under cursor
            '''

            pass

        def id_operation(type='UNLINK'):
            '''undocumented
               Arguments:
               @type (str): in ['UNLINK', 'LOCAL', 'SINGLE', 'DELETE', 'REMAP', 'ADD_FAKE', 'CLEAR_FAKE', 'RENAME', 'SELECT_LINKED'], (optional)

            '''

            pass

        def id_remap(id_type='OBJECT', old_id='', new_id=''):
            '''undocumented
               Arguments:
               @id_type (str): in ['ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'FONT', 'GREASEPENCIL', 'GROUP', 'IMAGE', 'KEY', 'LAMP', 'LIBRARY', 'LINESTYLE', 'LATTICE', 'MASK', 'MATERIAL', 'META', 'MESH', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'WINDOWMANAGER', 'WORLD'], (optional)
               @old_id (str): Old ID to replace
                  in [], (optional)
               @new_id (str): New ID to remap all selected IDs' users to
                  in [], (optional)

            '''

            pass

        def item_activate(extend=True, recursive=False):
            '''Handle mouse clicks to activate/select items
               Arguments:
               @extend (bool): Extend selection for activation
                  (optional)
               @recursive (bool): Select Objects and their children
                  (optional)

            '''

            pass

        def item_openclose(all=True):
            '''Toggle whether item under cursor is enabled or closed
               Arguments:
               @all (bool): Close or open all items
                  (optional)

            '''

            pass

        def item_rename():
            '''Rename item under cursor
            '''

            pass

        def keyingset_add_selected():
            '''Add selected items (blue-gray rows) to active Keying Set
            '''

            pass

        def keyingset_remove_selected():
            '''Remove selected items (blue-gray rows) from active Keying Set
            '''

            pass

        def lib_operation(type='RENAME'):
            '''undocumented
               Arguments:
               @type (str): in ['RENAME', 'DELETE', 'RELOCATE', 'RELOAD'], (optional)

            '''

            pass

        def lib_relocate():
            '''Relocate the library under cursor
            '''

            pass

        def material_drop(object="Object", material="Material"):
            '''Drag material to object in Outliner
               Arguments:
               @object (str): Target Object
                  (optional, never None)
               @material (str): Target Material
                  (optional, never None)

            '''

            pass

        def modifier_operation(type='TOGVIS'):
            '''undocumented
               Arguments:
               @type (str): in ['TOGVIS', 'TOGREN', 'DELETE'], (optional)

            '''

            pass

        def object_operation(type='SELECT'):
            '''undocumented
               Arguments:
               @type (str): in ['SELECT', 'DESELECT', 'SELECT_HIERARCHY', 'DELETE', 'DELETE_HIERARCHY', 'REMAP', 'TOGVIS', 'TOGSEL', 'TOGREN', 'RENAME'], (optional)

            '''

            pass

        def operation():
            '''Context menu for item operations
            '''

            pass

        def orphans_purge():
            '''Clear all orphaned datablocks without any users from the file (cannot be undone)
            '''

            pass

        def parent_clear(dragged_obj="Object", type='CLEAR'):
            '''Drag to clear parent in Outliner
               Arguments:
               @dragged_obj (str): Child Object
                  (optional, never None)
               @type (str): in ['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE'], (optional)

            '''

            pass

        def parent_drop(child="Object", parent="Object", type='OBJECT'):
            '''Drag to parent in Outliner
               Arguments:
               @child (str): Child Object
                  (optional, never None)
               @parent (str): Parent Object
                  (optional, never None)
               @type (str): in ['OBJECT', 'ARMATURE', 'ARMATURE_NAME', 'ARMATURE_AUTO', 'ARMATURE_ENVELOPE', 'BONE', 'BONE_RELATIVE', 'CURVE', 'FOLLOW', 'PATH_CONST', 'LATTICE', 'VERTEX', 'VERTEX_TRI'], (optional)

            '''

            pass

        def renderability_toggle():
            '''Toggle the renderability of selected items
            '''

            pass

        def scene_drop(object="Object", scene="Scene"):
            '''Drag object to scene in Outliner
               Arguments:
               @object (str): Target Object
                  (optional, never None)
               @scene (str): Target Scene
                  (optional, never None)

            '''

            pass

        def scene_operation(type='DELETE'):
            '''Context menu for scene operations
               Arguments:
               @type (str): in ['DELETE'], (optional)

            '''

            pass

        def scroll_page(up=False):
            '''Scroll page up or down
               Arguments:
               @up (bool): Scroll up one page
                  (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
            '''Use box selection to select tree elements
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def selectability_toggle():
            '''Toggle the selectability
            '''

            pass

        def selected_toggle():
            '''Toggle the Outliner selection of items
            '''

            pass

        def show_active():
            '''Open up the tree and adjust the view so that the active Object is shown centered
            '''

            pass

        def show_hierarchy():
            '''Open all object entries and close all others
            '''

            pass

        def show_one_level(open=True):
            '''Expand/collapse all entries by one level
               Arguments:
               @open (bool): Expand all entries one level deep
                  (optional)

            '''

            pass

        def visibility_toggle():
            '''Toggle the visibility of selected items
            '''

            pass

    class paint:
        '''Spcecial class, created just to reflect content of bpy.ops.paint'''

        def add_simple_uvs():
            '''Add cube map uvs on mesh
            '''

            pass

        def add_texture_paint_slot(type='DIFFUSE_COLOR', name="Untitled", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False):
            '''Add a texture paint slot
               Arguments:
               @type (str): Merge method to use
                  in ['DIFFUSE_COLOR', 'DIFFUSE_INTENSITY', 'ALPHA', 'TRANSLUCENCY', 'SPECULAR_COLOR', 'SPECULAR_INTENSITY', 'SPECULAR_HARDNESS', 'AMBIENT', 'EMIT', 'MIRROR_COLOR', 'RAYMIRROR', 'NORMAL', 'WARP', 'DISPLACE'], (optional)
               @name (str): Image datablock name
                  (optional, never None)
               @width (int): Image width
                  in [1, inf], (optional)
               @height (int): Image height
                  in [1, inf], (optional)
               @color (float): Default fill color
                  array of 4 items in [0, inf], (optional)
               @alpha (bool): Create an image with an alpha channel
                  (optional)
               @generated_type (str): Fill the image with a grid for UV map testing
                  in ['BLANK', 'UV_GRID', 'COLOR_GRID'], (optional)
               @float (bool): Create image with 32 bit floating point bit depth
                  (optional)

            '''

            pass

        def brush_colors_flip():
            '''Toggle foreground and background brush colors
            '''

            pass

        def brush_select(paint_mode='ACTIVE', sculpt_tool='BLOB', vertex_paint_tool='MIX', weight_paint_tool='MIX', texture_paint_tool='DRAW', toggle=False, create_missing=False):
            '''Select a paint mode's brush by tool type
               Arguments:
               @paint_mode (str): in ['ACTIVE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT'], (optional)
               @sculpt_tool (str): in ['BLOB', 'CLAY', 'CLAY_STRIPS', 'CREASE', 'DRAW', 'FILL', 'FLATTEN', 'GRAB', 'INFLATE', 'LAYER', 'MASK', 'NUDGE', 'PINCH', 'ROTATE', 'SCRAPE', 'SIMPLIFY', 'SMOOTH', 'SNAKE_HOOK', 'THUMB'], (optional)
               @vertex_paint_tool (str): in ['MIX', 'ADD', 'SUB', 'MUL', 'BLUR', 'LIGHTEN', 'DARKEN'], (optional)
               @weight_paint_tool (str): in ['MIX', 'ADD', 'SUB', 'MUL', 'BLUR', 'LIGHTEN', 'DARKEN'], (optional)
               @texture_paint_tool (str): in ['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK'], (optional)
               @toggle (bool): Toggle between two brushes rather than cycling
                  (optional)
               @create_missing (bool): If the requested brush type does not exist, create a new brush
                  (optional)

            '''

            pass

        def delete_texture_paint_slot():
            '''Delete selected texture paint slot
            '''

            pass

        def face_select_all(action='TOGGLE'):
            '''Change selection for all faces
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def face_select_hide(unselected=False):
            '''Hide selected faces
               Arguments:
               @unselected (bool): Hide unselected rather than selected objects
                  (optional)

            '''

            pass

        def face_select_linked():
            '''Select linked faces
            '''

            pass

        def face_select_linked_pick(deselect=False):
            '''Select linked faces under the cursor
               Arguments:
               @deselect (bool): Deselect rather than select items
                  (optional)

            '''

            pass

        def face_select_reveal(unselected=False):
            '''Reveal hidden faces
               Arguments:
               @unselected (bool): Hide unselected rather than selected objects
                  (optional)

            '''

            pass

        def grab_clone(delta=(0.0, 0.0)):
            '''Move the clone source image
               Arguments:
               @delta (float): Delta offset of clone image in 0.0..1.0 coordinates
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def hide_show(action='HIDE', area='INSIDE', xmin=0, xmax=0, ymin=0, ymax=0):
            '''Hide/show some vertices
               Arguments:
               @action (str): Whether to hide or show vertices
                  in ['HIDE', 'SHOW'], (optional)
               @area (str): Which vertices to hide or show
                  in ['OUTSIDE', 'INSIDE', 'ALL', 'MASKED'], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def image_from_view(filepath=""):
            '''Make an image from the current 3D view for re-projection
               Arguments:
               @filepath (str): Name of the file
                  (optional, never None)

            '''

            pass

        def image_paint(stroke=None, mode='NORMAL'):
            '''Paint a stroke into the image
               Arguments:
               @stroke (OperatorStrokeElement): Collection of , (optional)
               @mode (str): Action taken when a paint stroke is made
                  in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)

            '''

            pass

        def mask_flood_fill(mode='VALUE', value=0.0):
            '''Fill the whole mask with a given value, or invert its values
               Arguments:
               @mode (str): in ['VALUE', 'VALUE_INVERSE', 'INVERT'], (optional)
               @value (float): Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
                  in [0, 1], (optional)

            '''

            pass

        def mask_lasso_gesture(path=None, mode='VALUE', value=1.0):
            '''Add mask within the lasso as you move the brush
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @mode (str): in ['VALUE', 'VALUE_INVERSE', 'INVERT'], (optional)
               @value (float): Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
                  in [0, 1], (optional)

            '''

            pass

        def project_image(image=''):
            '''Project an edited render from the active camera back onto the object
               Arguments:
               @image (str): in [], (optional)

            '''

            pass

        def sample_color(location=(0, 0), merged=False, palette=False):
            '''Use the mouse to sample a color in the image
               Arguments:
               @location (int): array of 2 items in [0, inf], (optional)
               @merged (bool): Sample the output display color
                  (optional)
               @palette (bool): (optional)

            '''

            pass

        def texture_paint_toggle():
            '''Toggle texture paint mode in 3D view
            '''

            pass

        def vert_select_all(action='TOGGLE'):
            '''Change selection for all vertices
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def vert_select_ungrouped(extend=False):
            '''Select vertices without a group
               Arguments:
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def vertex_color_brightness_contrast(brightness=0.0, contrast=0.0):
            '''Adjust vertex color brightness/contrast
               Arguments:
               @brightness (float): in [-100, 100], (optional)
               @contrast (float): in [-100, 100], (optional)

            '''

            pass

        def vertex_color_dirt(blur_strength=1.0, blur_iterations=1, clean_angle=3.14159, dirt_angle=0.0, dirt_only=False):
            '''undocumented
               Arguments:
               @blur_strength (float): Blur strength per iteration
                  in [0.01, 1], (optional)
               @blur_iterations (int): Number of times to blur the colors (higher blurs more)
                  in [0, 40], (optional)
               @clean_angle (float): Less than 90 limits the angle used in the tonal range
                  in [0, 3.14159], (optional)
               @dirt_angle (float): Less than 90 limits the angle used in the tonal range
                  in [0, 3.14159], (optional)
               @dirt_only (bool): Don't calculate cleans for convex areas
                  (optional)

            '''

            pass

        def vertex_color_hsv(h=0.5, s=1.0, v=1.0):
            '''Adjust vertex color HSV values
               Arguments:
               @h (float): in [0, 1], (optional)
               @s (float): in [0, 2], (optional)
               @v (float): in [0, 2], (optional)

            '''

            pass

        def vertex_color_invert():
            '''Invert RGB values
            '''

            pass

        def vertex_color_levels(offset=0.0, gain=1.0):
            '''Adjust levels of vertex colors
               Arguments:
               @offset (float): Value to add to colors
                  in [-1, 1], (optional)
               @gain (float): Value to multiply colors by
                  in [0, inf], (optional)

            '''

            pass

        def vertex_color_set():
            '''Fill the active vertex color layer with the current paint color
            '''

            pass

        def vertex_color_smooth():
            '''Smooth colors across vertices
            '''

            pass

        def vertex_paint(stroke=None, mode='NORMAL'):
            '''Paint a stroke in the active vertex color layer
               Arguments:
               @stroke (OperatorStrokeElement): Collection of , (optional)
               @mode (str): Action taken when a paint stroke is made
                  in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)

            '''

            pass

        def vertex_paint_toggle():
            '''Toggle the vertex paint mode in 3D view
            '''

            pass

        def weight_from_bones(type='AUTOMATIC'):
            '''Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones
               Arguments:
               @type (str): Method to use for assigning weights
                  in ['AUTOMATIC', 'ENVELOPES'], (optional)

            '''

            pass

        def weight_gradient(type='LINEAR', xstart=0, xend=0, ystart=0, yend=0, cursor=1002):
            '''Draw a line to apply a weight gradient to selected vertices
               Arguments:
               @type (str): in ['LINEAR', 'RADIAL'], (optional)
               @xstart (int): in [-inf, inf], (optional)
               @xend (int): in [-inf, inf], (optional)
               @ystart (int): in [-inf, inf], (optional)
               @yend (int): in [-inf, inf], (optional)
               @cursor (int): Mouse cursor style to use during the modal operator
                  in [0, inf], (optional)

            '''

            pass

        def weight_paint(stroke=None, mode='NORMAL'):
            '''Paint a stroke in the current vertex group's weights
               Arguments:
               @stroke (OperatorStrokeElement): Collection of , (optional)
               @mode (str): Action taken when a paint stroke is made
                  in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)

            '''

            pass

        def weight_paint_toggle():
            '''Toggle weight paint mode in 3D view
            '''

            pass

        def weight_sample():
            '''Use the mouse to sample a weight in the 3D view
            '''

            pass

        def weight_sample_group(group='DEFAULT'):
            '''Select one of the vertex groups available under current mouse position
               Arguments:
               @group (str): The Keying Set to use
                  in ['DEFAULT'], (optional)

            '''

            pass

        def weight_set():
            '''Fill the active vertex group with the current paint weight
            '''

            pass

    class paintcurve:
        '''Spcecial class, created just to reflect content of bpy.ops.paintcurve'''

        def add_point(location=(0, 0)):
            '''Add New Paint Curve Point
               Arguments:
               @location (int): Location of vertex in area space
                  array of 2 items in [0, 32767], (optional)

            '''

            pass

        def add_point_slide(PAINTCURVE_OT_add_point=None, PAINTCURVE_OT_slide=None):
            '''Add new curve point and slide it
               Arguments:
               @PAINTCURVE_OT_add_point (PAINTCURVE_OT_add_point): Add New Paint Curve Point
                  (optional)
               @PAINTCURVE_OT_slide (PAINTCURVE_OT_slide): Select and slide paint curve point
                  (optional)

            '''

            pass

        def cursor():
            '''Place cursor
            '''

            pass

        def delete_point():
            '''Remove Paint Curve Point
            '''

            pass

        def draw():
            '''Draw curve
            '''

            pass

        def new():
            '''Add new paint curve
            '''

            pass

        def select(location=(0, 0), toggle=False, extend=False):
            '''Select a paint curve point
               Arguments:
               @location (int): Location of vertex in area space
                  array of 2 items in [0, 32767], (optional)
               @toggle (bool): (De)select all
                  (optional)
               @extend (bool): Extend selection
                  (optional)

            '''

            pass

        def slide(align=False, select=True):
            '''Select and slide paint curve point
               Arguments:
               @align (bool): Aligns opposite point handle during transform
                  (optional)
               @select (bool): Attempt to select a point handle before transform
                  (optional)

            '''

            pass

    class palette:
        '''Spcecial class, created just to reflect content of bpy.ops.palette'''

        def color_add():
            '''Add new color to active palette
            '''

            pass

        def color_delete():
            '''Remove active color from palette
            '''

            pass

        def new():
            '''Add new palette
            '''

            pass

    class particle:
        '''Spcecial class, created just to reflect content of bpy.ops.particle'''

        def brush_edit(stroke=None):
            '''Apply a stroke of brush to the particles
               Arguments:
               @stroke (OperatorStrokeElement): Collection of , (optional)

            '''

            pass

        def connect_hair(all=False):
            '''Connect hair to the emitter mesh
               Arguments:
               @all (bool): Connect all hair systems to the emitter mesh
                  (optional)

            '''

            pass

        def copy_particle_systems(space='OBJECT', remove_target_particles=True, use_active=False):
            '''Copy particle systems from the active object to selected objects
               Arguments:
               @space (str): Space transform for copying from one object to another
                  in ['OBJECT', 'WORLD'], (optional)
               @remove_target_particles (bool): Remove particle systems on the target objects
                  (optional)
               @use_active (bool): Use the active particle system from the context
                  (optional)

            '''

            pass

        def delete(type='PARTICLE'):
            '''Delete selected particles or keys
               Arguments:
               @type (str): Delete a full particle or only keys
                  in ['PARTICLE', 'KEY'], (optional)

            '''

            pass

        def disconnect_hair(all=False):
            '''Disconnect hair from the emitter mesh
               Arguments:
               @all (bool): Disconnect all hair systems from the emitter mesh
                  (optional)

            '''

            pass

        def dupliob_copy():
            '''Duplicate the current dupliobject
            '''

            pass

        def dupliob_move_down():
            '''Move dupli object down in the list
            '''

            pass

        def dupliob_move_up():
            '''Move dupli object up in the list
            '''

            pass

        def dupliob_remove():
            '''Remove the selected dupliobject
            '''

            pass

        def edited_clear():
            '''Undo all edition performed on the particle system
            '''

            pass

        def hair_dynamics_preset_add(name="", remove_active=False):
            '''Add or remove a Hair Dynamics Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def hide(unselected=False):
            '''Hide selected particles
               Arguments:
               @unselected (bool): Hide unselected rather than selected
                  (optional)

            '''

            pass

        def mirror():
            '''Duplicate and mirror the selected particles along the local X axis
            '''

            pass

        def new():
            '''Add new particle settings
            '''

            pass

        def new_target():
            '''Add a new particle target
            '''

            pass

        def particle_edit_toggle():
            '''Toggle particle edit mode
            '''

            pass

        def rekey(keys_number=2):
            '''Change the number of keys of selected particles (root and tip keys included)
               Arguments:
               @keys_number (int): in [2, inf], (optional)

            '''

            pass

        def remove_doubles(threshold=0.0002):
            '''Remove selected particles close enough of others
               Arguments:
               @threshold (float): Threshold distance withing which particles are removed
                  in [0, inf], (optional)

            '''

            pass

        def reveal():
            '''Show hidden particles
            '''

            pass

        def select_all(action='TOGGLE'):
            '''(De)select all particles' keys
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_less():
            '''Deselect boundary selected keys of each particle
            '''

            pass

        def select_linked(deselect=False, location=(0, 0)):
            '''Select nearest particle from mouse pointer
               Arguments:
               @deselect (bool): Deselect linked keys rather than selecting them
                  (optional)
               @location (int): array of 2 items in [0, inf], (optional)

            '''

            pass

        def select_more():
            '''Select keys linked to boundary selected keys of each particle
            '''

            pass

        def select_random(percent=50.0, seed=0, action='SELECT', type='HAIR'):
            '''Select a randomly distributed set of hair or points
               Arguments:
               @percent (float): Percentage of objects to select randomly
                  in [0, 100], (optional)
               @seed (int): Seed for the random number generator
                  in [0, inf], (optional)
               @action (str): Selection action to execute
                  in ['SELECT', 'DESELECT'], (optional)
               @type (str): Select either hair or points
                  in ['HAIR', 'POINTS'], (optional)

            '''

            pass

        def select_roots(action='SELECT'):
            '''Select roots of all visible particles
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_tips(action='SELECT'):
            '''Select tips of all visible particles
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def shape_cut():
            '''Cut hair to conform to the set shape object
            '''

            pass

        def subdivide():
            '''Subdivide selected particles segments (adds keys)
            '''

            pass

        def target_move_down():
            '''Move particle target down in the list
            '''

            pass

        def target_move_up():
            '''Move particle target up in the list
            '''

            pass

        def target_remove():
            '''Remove the selected particle target
            '''

            pass

        def unify_length():
            '''Make selected hair the same length
            '''

            pass

        def weight_set(factor=1.0):
            '''Set the weight of selected keys
               Arguments:
               @factor (float): Interpolation factor between current brush weight, and keys' weights
                  in [0, 1], (optional)

            '''

            pass

    class pose:
        '''Spcecial class, created just to reflect content of bpy.ops.pose'''

        def armature_apply():
            '''Apply the current pose as the new rest pose
            '''

            pass

        def autoside_names(axis='XAXIS'):
            '''Automatically renames the selected bones according to which side of the target axis they fall on
               Arguments:
               @axis (str): Axis tag names with
                  in ['XAXIS', 'YAXIS', 'ZAXIS'], (optional)

            '''

            pass

        def bone_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Change the layers that the selected bones belong to
               Arguments:
               @layers (bool): Armature layers that bone belongs to
                  array of 32 items, (optional)

            '''

            pass

        def breakdown(prev_frame=0, next_frame=0, percentage=0.5):
            '''Create a suitable breakdown pose on the current frame
               Arguments:
               @prev_frame (int): Frame number of keyframe immediately before the current frame
                  in [-500000, 500000], (optional)
               @next_frame (int): Frame number of keyframe immediately after the current frame
                  in [-500000, 500000], (optional)
               @percentage (float): Weighting factor for the sliding operation
                  in [0, 1], (optional)

            '''

            pass

        def constraint_add(type=''):
            '''Add a constraint to the active bone
               Arguments:
               @type (str): in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'RIGID_BODY_JOINT', 'SHRINKWRAP'], (optional)

            '''

            pass

        def constraint_add_with_targets(type=''):
            '''Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones
               Arguments:
               @type (str): in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'RIGID_BODY_JOINT', 'SHRINKWRAP'], (optional)

            '''

            pass

        def constraints_clear():
            '''Clear all the constraints for the selected bones
            '''

            pass

        def constraints_copy():
            '''Copy constraints to other selected bones
            '''

            pass

        def copy():
            '''Copies the current pose of the selected bones to copy/paste buffer
            '''

            pass

        def flip_names():
            '''Flips (and corrects) the axis suffixes of the names of selected bones
            '''

            pass

        def group_add():
            '''Add a new bone group
            '''

            pass

        def group_assign(type=0):
            '''Add selected bones to the chosen bone group
               Arguments:
               @type (int): in [0, inf], (optional)

            '''

            pass

        def group_deselect():
            '''Deselect bones of active Bone Group
            '''

            pass

        def group_move(direction='UP'):
            '''Change position of active Bone Group in list of Bone Groups
               Arguments:
               @direction (str): Direction to move, UP or DOWN
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def group_remove():
            '''Remove the active bone group
            '''

            pass

        def group_select():
            '''Select bones in active Bone Group
            '''

            pass

        def group_sort():
            '''Sort Bone Groups by their names in ascending order
            '''

            pass

        def group_unassign():
            '''Remove selected bones from all bone groups
            '''

            pass

        def hide(unselected=False):
            '''Tag selected bones to not be visible in Pose Mode
               Arguments:
               @unselected (bool): (optional)

            '''

            pass

        def ik_add(with_targets=True):
            '''Add IK Constraint to the active Bone
               Arguments:
               @with_targets (bool): Assign IK Constraint with targets derived from the select bones/objects
                  (optional)

            '''

            pass

        def ik_clear():
            '''Remove all IK Constraints from selected bones
            '''

            pass

        def loc_clear():
            '''Reset locations of selected bones to their default values
            '''

            pass

        def paste(flipped=False, selected_mask=False):
            '''Paste the stored pose on to the current pose
               Arguments:
               @flipped (bool): Paste the stored pose flipped on to current pose
                  (optional)
               @selected_mask (bool): Only paste the stored pose on to selected bones in the current pose
                  (optional)

            '''

            pass

        def paths_calculate(start_frame=1, end_frame=250, bake_location='TAILS'):
            '''Calculate paths for the selected bones
               Arguments:
               @start_frame (int): First frame to calculate bone paths on
                  in [-500000, 500000], (optional)
               @end_frame (int): Last frame to calculate bone paths on
                  in [-500000, 500000], (optional)
               @bake_location (str): Which point on the bones is used when calculating paths
                  in ['HEADS', 'TAILS'], (optional)

            '''

            pass

        def paths_clear(only_selected=False):
            '''Clear path caches for all bones, hold Shift key for selected bones only
               Arguments:
               @only_selected (bool): Only clear paths from selected bones
                  (optional)

            '''

            pass

        def paths_update():
            '''Recalculate paths for bones that already have them
            '''

            pass

        def propagate(mode='WHILE_HELD', end_frame=250.0):
            '''Copy selected aspects of the current pose to subsequent poses already keyframed
               Arguments:
               @mode (str): Method used to determine when to stop propagating pose to keyframes
                  in ['WHILE_HELD', 'NEXT_KEY', 'LAST_KEY', 'BEFORE_FRAME', 'BEFORE_END', 'SELECTED_KEYS', 'SELECTED_MARKERS'], (optional)
               @end_frame (float): Frame to stop propagating frames to (for 'Before Frame' mode)
                  in [1.17549e-38, inf], (optional)

            '''

            pass

        def push(prev_frame=0, next_frame=0, percentage=0.5):
            '''Exaggerate the current pose
               Arguments:
               @prev_frame (int): Frame number of keyframe immediately before the current frame
                  in [-500000, 500000], (optional)
               @next_frame (int): Frame number of keyframe immediately after the current frame
                  in [-500000, 500000], (optional)
               @percentage (float): Weighting factor for the sliding operation
                  in [0, 1], (optional)

            '''

            pass

        def quaternions_flip():
            '''Flip quaternion values to achieve desired rotations, while maintaining the same orientations
            '''

            pass

        def relax(prev_frame=0, next_frame=0, percentage=0.5):
            '''Make the current pose more similar to its surrounding ones
               Arguments:
               @prev_frame (int): Frame number of keyframe immediately before the current frame
                  in [-500000, 500000], (optional)
               @next_frame (int): Frame number of keyframe immediately after the current frame
                  in [-500000, 500000], (optional)
               @percentage (float): Weighting factor for the sliding operation
                  in [0, 1], (optional)

            '''

            pass

        def reveal():
            '''Unhide all bones that have been tagged to be hidden in Pose Mode
            '''

            pass

        def rot_clear():
            '''Reset rotations of selected bones to their default values
            '''

            pass

        def rotation_mode_set(type='QUATERNION'):
            '''Set the rotation representation used by selected bones
               Arguments:
               @type (str): in ['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE'], (optional)

            '''

            pass

        def scale_clear():
            '''Reset scaling of selected bones to their default values
            '''

            pass

        def select_all(action='TOGGLE'):
            '''Toggle selection status of all bones
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_constraint_target():
            '''Select bones used as targets for the currently selected bones
            '''

            pass

        def select_grouped(extend=False, type='LAYER'):
            '''Select all visible bones grouped by similar properties
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @type (str): in ['LAYER', 'GROUP', 'KEYINGSET'], (optional)

            '''

            pass

        def select_hierarchy(direction='PARENT', extend=False):
            '''Select immediate parent/children of selected bones
               Arguments:
               @direction (str): in ['PARENT', 'CHILD'], (optional)
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_linked(extend=False):
            '''Select bones related to selected ones by parent/child relationships
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_mirror(only_active=False, extend=False):
            '''Mirror the bone selection
               Arguments:
               @only_active (bool): Only operate on the active bone
                  (optional)
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_parent():
            '''Select bones that are parents of the currently selected bones
            '''

            pass

        def transforms_clear():
            '''Reset location, rotation, and scaling of selected bones to their default values
            '''

            pass

        def user_transforms_clear(only_selected=True):
            '''Reset pose on selected bones to keyframed state
               Arguments:
               @only_selected (bool): Only visible/selected bones
                  (optional)

            '''

            pass

        def visual_transform_apply():
            '''Apply final constrained position of pose bones to their transform
            '''

            pass

    class poselib:
        '''Spcecial class, created just to reflect content of bpy.ops.poselib'''

        def action_sanitize():
            '''Make action suitable for use as a Pose Library
            '''

            pass

        def apply_pose(pose_index=-1):
            '''Apply specified Pose Library pose to the rig
               Arguments:
               @pose_index (int): Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
                  in [-2, inf], (optional)

            '''

            pass

        def browse_interactive(pose_index=-1):
            '''Interactively browse poses in 3D-View
               Arguments:
               @pose_index (int): Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
                  in [-2, inf], (optional)

            '''

            pass

        def new():
            '''Add New Pose Library to active Object
            '''

            pass

        def pose_add(frame=1, name="Pose"):
            '''Add the current Pose to the active Pose Library
               Arguments:
               @frame (int): Frame to store pose on
                  in [0, inf], (optional)
               @name (str): Name of newly added Pose
                  (optional, never None)

            '''

            pass

        def pose_remove(pose=''):
            '''Remove nth pose from the active Pose Library
               Arguments:
               @pose (str): The pose to remove
                  in [], (optional)

            '''

            pass

        def pose_rename(name="RenamedPose", pose=''):
            '''Rename specified pose from the active Pose Library
               Arguments:
               @name (str): New name for pose
                  (optional, never None)
               @pose (str): The pose to rename
                  in [], (optional)

            '''

            pass

        def unlink():
            '''Remove Pose Library from active Object
            '''

            pass

    class ptcache:
        '''Spcecial class, created just to reflect content of bpy.ops.ptcache'''

        def add():
            '''Add new cache
            '''

            pass

        def bake(bake=False):
            '''Bake physics
               Arguments:
               @bake (bool): (optional)

            '''

            pass

        def bake_all(bake=True):
            '''Bake all physics
               Arguments:
               @bake (bool): (optional)

            '''

            pass

        def bake_from_cache():
            '''Bake from cache
            '''

            pass

        def free_bake():
            '''Free physics bake
            '''

            pass

        def free_bake_all():
            '''Free all baked caches of all objects in the current scene
            '''

            pass

        def remove():
            '''Delete current cache
            '''

            pass

    class render:
        '''Spcecial class, created just to reflect content of bpy.ops.render'''

        def cycles_integrator_preset_add(name="", remove_active=False):
            '''Add an Integrator Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def cycles_sampling_preset_add(name="", remove_active=False):
            '''Add a Sampling Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def opengl(animation=False, sequencer=False, write_still=False, view_context=True):
            '''OpenGL render active viewport
               Arguments:
               @animation (bool): Render files from the animation range of this scene
                  (optional)
               @sequencer (bool): Render using the sequencer's OpenGL display
                  (optional)
               @write_still (bool): Save rendered the image to the output path (used only when animation is disabled)
                  (optional)
               @view_context (bool): Use the current 3D view for rendering, else use scene settings
                  (optional)

            '''

            pass

        def play_rendered_anim():
            '''Play back rendered frames/movies using an external player
            '''

            pass

        def preset_add(name="", remove_active=False):
            '''Add or remove a Render Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def render(animation=False, write_still=False, use_viewport=False, layer="", scene=""):
            '''Render active scene
               Arguments:
               @animation (bool): Render files from the animation range of this scene
                  (optional)
               @write_still (bool): Save rendered the image to the output path (used only when animation is disabled)
                  (optional)
               @use_viewport (bool): When inside a 3D viewport, use layers and camera of the viewport
                  (optional)
               @layer (str): Single render layer to re-render (used only when animation is disabled)
                  (optional, never None)
               @scene (str): Scene to render, current scene if not specified
                  (optional, never None)

            '''

            pass

        def shutter_curve_preset(shape='SMOOTH'):
            '''Set shutter curve
               Arguments:
               @shape (str): in ['SHARP', 'SMOOTH', 'MAX', 'LINE', 'ROUND', 'ROOT'], (optional)

            '''

            pass

        def view_cancel():
            '''Cancel show render view
            '''

            pass

        def view_show():
            '''Toggle show render view
            '''

            pass

    class rigidbody:
        '''Spcecial class, created just to reflect content of bpy.ops.rigidbody'''

        def bake_to_keyframes(frame_start=1, frame_end=250, step=1):
            '''Bake rigid body transformations of selected objects to keyframes
               Arguments:
               @frame_start (int): Start frame for baking
                  in [0, 300000], (optional)
               @frame_end (int): End frame for baking
                  in [1, 300000], (optional)
               @step (int): Frame Step
                  in [1, 120], (optional)

            '''

            pass

        def connect(con_type='FIXED', pivot_type='CENTER', connection_pattern='SELECTED_TO_ACTIVE'):
            '''Create rigid body constraints between selected rigid bodies
               Arguments:
               @con_type (str): Type of generated constraint
                  in ['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], (optional)
               @pivot_type (str): Constraint pivot location
                  in ['CENTER', 'ACTIVE', 'SELECTED'], (optional)
               @connection_pattern (str): Pattern used to connect objects
                  in ['SELECTED_TO_ACTIVE', 'CHAIN_DISTANCE'], (optional)

            '''

            pass

        def constraint_add(type='FIXED'):
            '''Add Rigid Body Constraint to active object
               Arguments:
               @type (str): in ['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], (optional)

            '''

            pass

        def constraint_remove():
            '''Remove Rigid Body Constraint from Object
            '''

            pass

        def mass_calculate(material='DEFAULT', density=1.0):
            '''Automatically calculate mass values for Rigid Body Objects based on volume
               Arguments:
               @material (str): Type of material that objects are made of (determines material density)
                  in ['DEFAULT'], (optional)
               @density (float): Custom density value (kg/m^3) to use instead of material preset
                  in [1.17549e-38, inf], (optional)

            '''

            pass

        def object_add(type='ACTIVE'):
            '''Add active object as Rigid Body
               Arguments:
               @type (str): in ['ACTIVE', 'PASSIVE'], (optional)

            '''

            pass

        def object_remove():
            '''Remove Rigid Body settings from Object
            '''

            pass

        def object_settings_copy():
            '''Copy Rigid Body settings from active object to selected
            '''

            pass

        def objects_add(type='ACTIVE'):
            '''Add selected objects as Rigid Bodies
               Arguments:
               @type (str): in ['ACTIVE', 'PASSIVE'], (optional)

            '''

            pass

        def objects_remove():
            '''Remove selected objects from Rigid Body simulation
            '''

            pass

        def shape_change(type='MESH'):
            '''Change collision shapes for selected Rigid Body Objects
               Arguments:
               @type (str): in ['BOX', 'SPHERE', 'CAPSULE', 'CYLINDER', 'CONE', 'CONVEX_HULL', 'MESH'], (optional)

            '''

            pass

        def world_add():
            '''Add Rigid Body simulation world to the current scene
            '''

            pass

        def world_remove():
            '''Remove Rigid Body simulation world from the current scene
            '''

            pass

    class safe_areas:
        '''Spcecial class, created just to reflect content of bpy.ops.safe_areas'''

        def preset_add(name="", remove_active=False):
            '''Add or remove a Safe Areas Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

    class scene:
        '''Spcecial class, created just to reflect content of bpy.ops.scene'''

        def delete():
            '''Delete active scene
            '''

            pass

        def freestyle_add_edge_marks_to_keying_set():
            '''Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set
            '''

            pass

        def freestyle_add_face_marks_to_keying_set():
            '''Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set
            '''

            pass

        def freestyle_alpha_modifier_add(type='ALONG_STROKE'):
            '''Add an alpha transparency modifier to the line style associated with the active lineset
               Arguments:
               @type (str): in ['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)

            '''

            pass

        def freestyle_color_modifier_add(type='ALONG_STROKE'):
            '''Add a line color modifier to the line style associated with the active lineset
               Arguments:
               @type (str): in ['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)

            '''

            pass

        def freestyle_fill_range_by_selection(type='COLOR', name=""):
            '''Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object
               Arguments:
               @type (str): Type of the modifier to work on
                  in ['COLOR', 'ALPHA', 'THICKNESS'], (optional)
               @name (str): Name of the modifier to work on
                  (optional, never None)

            '''

            pass

        def freestyle_geometry_modifier_add(type='2D_OFFSET'):
            '''Add a stroke geometry modifier to the line style associated with the active lineset
               Arguments:
               @type (str): in ['2D_OFFSET', '2D_TRANSFORM', 'BACKBONE_STRETCHER', 'BEZIER_CURVE', 'BLUEPRINT', 'GUIDING_LINES', 'PERLIN_NOISE_1D', 'PERLIN_NOISE_2D', 'POLYGONIZATION', 'SAMPLING', 'SIMPLIFICATION', 'SINUS_DISPLACEMENT', 'SPATIAL_NOISE', 'TIP_REMOVER'], (optional)

            '''

            pass

        def freestyle_lineset_add():
            '''Add a line set into the list of line sets
            '''

            pass

        def freestyle_lineset_copy():
            '''Copy the active line set to a buffer
            '''

            pass

        def freestyle_lineset_move(direction='UP'):
            '''Change the position of the active line set within the list of line sets
               Arguments:
               @direction (str): Direction to move, UP or DOWN
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def freestyle_lineset_paste():
            '''Paste the buffer content to the active line set
            '''

            pass

        def freestyle_lineset_remove():
            '''Remove the active line set from the list of line sets
            '''

            pass

        def freestyle_linestyle_new():
            '''Create a new line style, reusable by multiple line sets
            '''

            pass

        def freestyle_modifier_copy():
            '''Duplicate the modifier within the list of modifiers
            '''

            pass

        def freestyle_modifier_move(direction='UP'):
            '''Move the modifier within the list of modifiers
               Arguments:
               @direction (str): Direction to move, UP or DOWN
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def freestyle_modifier_remove():
            '''Remove the modifier from the list of modifiers
            '''

            pass

        def freestyle_module_add():
            '''Add a style module into the list of modules
            '''

            pass

        def freestyle_module_move(direction='UP'):
            '''Change the position of the style module within in the list of style modules
               Arguments:
               @direction (str): Direction to move, UP or DOWN
                  in ['UP', 'DOWN'], (optional)

            '''

            pass

        def freestyle_module_open(filepath="", make_internal=True):
            '''Open a style module file
               Arguments:
               @filepath (str): (optional, never None)
               @make_internal (bool): Make module file internal after loading
                  (optional)

            '''

            pass

        def freestyle_module_remove():
            '''Remove the style module from the stack
            '''

            pass

        def freestyle_stroke_material_create():
            '''Create Freestyle stroke material for testing
            '''

            pass

        def freestyle_thickness_modifier_add(type='ALONG_STROKE'):
            '''Add a line thickness modifier to the line style associated with the active lineset
               Arguments:
               @type (str): in ['ALONG_STROKE', 'CALLIGRAPHY', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)

            '''

            pass

        def new(type='NEW'):
            '''Add new scene by type
               Arguments:
               @type (str): in ['NEW', 'EMPTY', 'LINK_OBJECTS', 'LINK_OBJECT_DATA', 'FULL_COPY'], (optional)

            '''

            pass

        def render_layer_add():
            '''Add a render layer
            '''

            pass

        def render_layer_remove():
            '''Remove the selected render layer
            '''

            pass

        def render_view_add():
            '''Add a render view
            '''

            pass

        def render_view_remove():
            '''Remove the selected render view
            '''

            pass

        def units_length_preset_add(name="", remove_active=False):
            '''Add or remove length units preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

    class screen:
        '''Spcecial class, created just to reflect content of bpy.ops.screen'''

        def actionzone(modifier=0):
            '''Handle area action zones for mouse actions/gestures
               Arguments:
               @modifier (int): Modifier state
                  in [0, 2], (optional)

            '''

            pass

        def animation_cancel(restore_frame=True):
            '''Cancel animation, returning to the original frame
               Arguments:
               @restore_frame (bool): Restore the frame when animation was initialized
                  (optional)

            '''

            pass

        def animation_play(reverse=False, sync=False):
            '''Play animation
               Arguments:
               @reverse (bool): Animation is played backwards
                  (optional)
               @sync (bool): Drop frames to maintain framerate
                  (optional)

            '''

            pass

        def animation_step():
            '''Step through animation by position
            '''

            pass

        def area_dupli():
            '''Duplicate selected area into new window
            '''

            pass

        def area_join(min_x=-100, min_y=-100, max_x=-100, max_y=-100):
            '''Join selected areas into new window
               Arguments:
               @min_x (int): in [-inf, inf], (optional)
               @min_y (int): in [-inf, inf], (optional)
               @max_x (int): in [-inf, inf], (optional)
               @max_y (int): in [-inf, inf], (optional)

            '''

            pass

        def area_move(x=0, y=0, delta=0):
            '''Move selected area edges
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @delta (int): in [-inf, inf], (optional)

            '''

            pass

        def area_options():
            '''Operations for splitting and merging
            '''

            pass

        def area_split(direction='HORIZONTAL', factor=0.5, mouse_x=-100, mouse_y=-100):
            '''Split selected area into new windows
               Arguments:
               @direction (str): in ['HORIZONTAL', 'VERTICAL'], (optional)
               @factor (float): in [0, 1], (optional)
               @mouse_x (int): in [-inf, inf], (optional)
               @mouse_y (int): in [-inf, inf], (optional)

            '''

            pass

        def area_swap():
            '''Swap selected areas screen positions
            '''

            pass

        def back_to_previous():
            '''Revert back to the original screen layout, before fullscreen area overlay
            '''

            pass

        def delete():
            '''Delete active screen
            '''

            pass

        def frame_jump(end=False):
            '''Jump to first/last frame in frame range
               Arguments:
               @end (bool): Jump to the last frame of the frame range
                  (optional)

            '''

            pass

        def frame_offset(delta=0):
            '''Move current frame forward/backward by a given number
               Arguments:
               @delta (int): in [-inf, inf], (optional)

            '''

            pass

        def header():
            '''Toggle header display
            '''

            pass

        def header_flip():
            '''Toggle the header over/below the main window area
            '''

            pass

        def header_toggle_menus():
            '''Expand or collapse the header pulldown menus
            '''

            pass

        def header_toolbox():
            '''Display header region toolbox
            '''

            pass

        def keyframe_jump(next=True):
            '''Jump to previous/next keyframe
               Arguments:
               @next (bool): (optional)

            '''

            pass

        def marker_jump(next=True):
            '''Jump to previous/next marker
               Arguments:
               @next (bool): (optional)

            '''

            pass

        def new():
            '''Add a new screen
            '''

            pass

        def redo_last():
            '''Display menu for last action performed
            '''

            pass

        def region_blend():
            '''Blend in and out overlapping region
            '''

            pass

        def region_flip():
            '''Toggle the region's alignment (left/right or top/bottom)
            '''

            pass

        def region_quadview():
            '''Split selected area into camera, front, right & top views
            '''

            pass

        def region_scale():
            '''Scale selected area
            '''

            pass

        def repeat_history(index=0):
            '''Display menu for previous actions performed
               Arguments:
               @index (int): in [0, inf], (optional)

            '''

            pass

        def repeat_last():
            '''Repeat last action
            '''

            pass

        def screen_full_area(use_hide_panels=False):
            '''Toggle display selected area as fullscreen/maximized
               Arguments:
               @use_hide_panels (bool): Hide all the panels
                  (optional)

            '''

            pass

        def screen_set(delta=0):
            '''Cycle through available screens
               Arguments:
               @delta (int): in [-inf, inf], (optional)

            '''

            pass

        def screencast(filepath="", full=True):
            '''Capture a video of the active area or whole Blender window
               Arguments:
               @filepath (str): (optional, never None)
               @full (bool): Capture the whole window (otherwise only capture the active area)
                  (optional)

            '''

            pass

        def screenshot(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', full=True):
            '''Capture a picture of the active area or whole Blender window
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @full (bool): Capture the whole window (otherwise only capture the active area)
                  (optional)

            '''

            pass

        def spacedata_cleanup():
            '''Remove unused settings for invisible editors
            '''

            pass

        def userpref_show():
            '''Show user preferences
            '''

            pass

    class script:
        '''Spcecial class, created just to reflect content of bpy.ops.script'''

        def autoexec_warn_clear():
            '''Ignore autoexec warning
            '''

            pass

        def execute_preset(filepath="", menu_idname=""):
            '''Execute a preset
               Arguments:
               @filepath (str): (optional, never None)
               @menu_idname (str): ID name of the menu this was called from
                  (optional, never None)

            '''

            pass

        def python_file_run(filepath=""):
            '''Run Python file
               Arguments:
               @filepath (str): (optional, never None)

            '''

            pass

        def reload():
            '''Reload Scripts
            '''

            pass

    class sculpt:
        '''Spcecial class, created just to reflect content of bpy.ops.sculpt'''

        def brush_stroke(stroke=None, mode='NORMAL', ignore_background_click=False):
            '''Sculpt a stroke into the geometry
               Arguments:
               @stroke (OperatorStrokeElement): Collection of , (optional)
               @mode (str): Action taken when a paint stroke is made
                  in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)
               @ignore_background_click (bool): Clicks on the background do not start the stroke
                  (optional)

            '''

            pass

        def detail_flood_fill():
            '''Flood fill the mesh with the selected detail setting
            '''

            pass

        def dynamic_topology_toggle():
            '''Dynamic topology alters the mesh topology while sculpting
            '''

            pass

        def optimize():
            '''Recalculate the sculpt BVH to improve performance
            '''

            pass

        def sample_detail_size(location=(0, 0)):
            '''Sample the mesh detail on clicked point
               Arguments:
               @location (int): Screen Coordinates of sampling
                  array of 2 items in [0, 32767], (optional)

            '''

            pass

        def sculptmode_toggle():
            '''Toggle sculpt mode in 3D view
            '''

            pass

        def set_detail_size():
            '''Set the mesh detail (either relative or constant one, depending on current dyntopo mode)
            '''

            pass

        def set_persistent_base():
            '''Reset the copy of the mesh that is being sculpted on
            '''

            pass

        def symmetrize():
            '''Symmetrize the topology modifications
            '''

            pass

        def uv_sculpt_stroke(mode='NORMAL'):
            '''Sculpt UVs using a brush
               Arguments:
               @mode (str): Stroke Mode
                  in ['NORMAL', 'INVERT', 'RELAX'], (optional)

            '''

            pass

    class sequencer:
        '''Spcecial class, created just to reflect content of bpy.ops.sequencer'''

        def change_effect_input(swap='A_B'):
            '''undocumented
               Arguments:
               @swap (str): The effect inputs to swap
                  in ['A_B', 'B_C', 'A_C'], (optional)

            '''

            pass

        def change_effect_type(type='CROSS'):
            '''undocumented
               Arguments:
               @type (str): Sequencer effect type
                  in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT'], (optional)

            '''

            pass

        def change_path(filepath="", directory="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', use_placeholders=False):
            '''undocumented
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @directory (str): Directory of the file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @use_placeholders (bool): Use placeholders for missing frames of the strip
                  (optional)

            '''

            pass

        def copy():
            '''undocumented
            '''

            pass

        def crossfade_sounds():
            '''Do cross-fading volume animation of two selected sound strips
            '''

            pass

        def cut(frame=0, type='SOFT', side='BOTH'):
            '''Cut the selected strips
               Arguments:
               @frame (int): Frame where selected strips will be cut
                  in [-inf, inf], (optional)
               @type (str): The type of cut operation to perform on strips
                  in ['SOFT', 'HARD'], (optional)
               @side (str): The side that remains selected after cutting
                  in ['LEFT', 'RIGHT', 'BOTH'], (optional)

            '''

            pass

        def cut_multicam(camera=1):
            '''Cut multi-cam strip and select camera
               Arguments:
               @camera (int): in [1, 32], (optional)

            '''

            pass

        def deinterlace_selected_movies():
            '''Deinterlace all selected movie sources
            '''

            pass

        def delete():
            '''Erase selected strips from the sequencer
            '''

            pass

        def duplicate(mode='TRANSLATION'):
            '''Duplicate the selected strips
               Arguments:
               @mode (str): in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)

            '''

            pass

        def duplicate_move(SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None):
            '''Duplicate selected strips and move them
               Arguments:
               @SEQUENCER_OT_duplicate (SEQUENCER_OT_duplicate): Duplicate the selected strips
                  (optional)
               @TRANSFORM_OT_seq_slide (TRANSFORM_OT_seq_slide): Slide a sequence strip in time
                  (optional)

            '''

            pass

        def effect_strip_add(frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, type='CROSS', color=(0.0, 0.0, 0.0)):
            '''Add an effect to the sequencer, most are applied on top of existing strips
               Arguments:
               @frame_start (int): Start frame of the sequence strip
                  in [-inf, inf], (optional)
               @frame_end (int): End frame for the color strip
                  in [-inf, inf], (optional)
               @channel (int): Channel to place this strip into
                  in [1, 32], (optional)
               @replace_sel (bool): Replace the current selection
                  (optional)
               @overlap (bool): Don't correct overlap on new sequence strips
                  (optional)
               @type (str): Sequencer effect type
                  in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT'], (optional)
               @color (float): Initialize the strip with this color (only used when type='COLOR')
                  array of 3 items in [0, 1], (optional)

            '''

            pass

        def enable_proxies(proxy_25=False, proxy_50=False, proxy_75=False, proxy_100=False, override=False):
            '''Enable selected proxies on all selected Movie strips
               Arguments:
               @proxy_25 (bool): (optional)
               @proxy_50 (bool): (optional)
               @proxy_75 (bool): (optional)
               @proxy_100 (bool): (optional)
               @override (bool): (optional)

            '''

            pass

        def export_subtitles(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Export .srt file containing text strips
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def gap_insert(frames=10):
            '''Insert gap at current frame to first strips at the right, independent of selection or locked state of strips
               Arguments:
               @frames (int): Frames to insert after current strip
                  in [0, inf], (optional)

            '''

            pass

        def gap_remove(all=False):
            '''Remove gap at current frame to first strip at the right, independent of selection or locked state of strips
               Arguments:
               @all (bool): Do all gaps to right of current frame
                  (optional)

            '''

            pass

        def image_strip_add(directory="", files=None, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, use_placeholders=False):
            '''Add an image or image sequence to the sequencer
               Arguments:
               @directory (str): Directory of the file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @frame_start (int): Start frame of the sequence strip
                  in [-inf, inf], (optional)
               @frame_end (int): End frame for the color strip
                  in [-inf, inf], (optional)
               @channel (int): Channel to place this strip into
                  in [1, 32], (optional)
               @replace_sel (bool): Replace the current selection
                  (optional)
               @overlap (bool): Don't correct overlap on new sequence strips
                  (optional)
               @use_placeholders (bool): Use placeholders for missing frames of the strip
                  (optional)

            '''

            pass

        def images_separate(length=1):
            '''On image sequence strips, it returns a strip for each image
               Arguments:
               @length (int): Length of each frame
                  in [1, inf], (optional)

            '''

            pass

        def lock():
            '''Lock the active strip so that it can't be transformed
            '''

            pass

        def mask_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, mask=''):
            '''Add a mask strip to the sequencer
               Arguments:
               @frame_start (int): Start frame of the sequence strip
                  in [-inf, inf], (optional)
               @channel (int): Channel to place this strip into
                  in [1, 32], (optional)
               @replace_sel (bool): Replace the current selection
                  (optional)
               @overlap (bool): Don't correct overlap on new sequence strips
                  (optional)
               @mask (str): in [], (optional)

            '''

            pass

        def meta_make():
            '''Group selected strips into a metastrip
            '''

            pass

        def meta_separate():
            '''Put the contents of a metastrip back in the sequencer
            '''

            pass

        def meta_toggle():
            '''Toggle a metastrip (to edit enclosed strips)
            '''

            pass

        def movie_strip_add(filepath="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, channel=1, replace_sel=True, overlap=False, sound=True, use_framerate=True):
            '''Add a movie strip to the sequencer
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @frame_start (int): Start frame of the sequence strip
                  in [-inf, inf], (optional)
               @channel (int): Channel to place this strip into
                  in [1, 32], (optional)
               @replace_sel (bool): Replace the current selection
                  (optional)
               @overlap (bool): Don't correct overlap on new sequence strips
                  (optional)
               @sound (bool): Load sound with the movie
                  (optional)
               @use_framerate (bool): Use framerate from the movie to keep sound and video in sync
                  (optional)

            '''

            pass

        def movieclip_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, clip=''):
            '''Add a movieclip strip to the sequencer
               Arguments:
               @frame_start (int): Start frame of the sequence strip
                  in [-inf, inf], (optional)
               @channel (int): Channel to place this strip into
                  in [1, 32], (optional)
               @replace_sel (bool): Replace the current selection
                  (optional)
               @overlap (bool): Don't correct overlap on new sequence strips
                  (optional)
               @clip (str): in [], (optional)

            '''

            pass

        def mute(unselected=False):
            '''Mute (un)selected strips
               Arguments:
               @unselected (bool): Mute unselected rather than selected strips
                  (optional)

            '''

            pass

        def offset_clear():
            '''Clear strip offsets from the start and end frames
            '''

            pass

        def paste():
            '''undocumented
            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def reassign_inputs():
            '''Reassign the inputs for the effect strip
            '''

            pass

        def rebuild_proxy():
            '''Rebuild all selected proxies and timecode indices using the job system
            '''

            pass

        def refresh_all():
            '''Refresh the sequencer editor
            '''

            pass

        def reload(adjust_length=False):
            '''Reload strips in the sequencer
               Arguments:
               @adjust_length (bool): Adjust length of strips to their data length
                  (optional)

            '''

            pass

        def rendersize():
            '''Set render size and aspect from active sequence
            '''

            pass

        def sample():
            '''Use mouse to sample color in current frame
            '''

            pass

        def scene_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, scene=''):
            '''Add a strip to the sequencer using a blender scene as a source
               Arguments:
               @frame_start (int): Start frame of the sequence strip
                  in [-inf, inf], (optional)
               @channel (int): Channel to place this strip into
                  in [1, 32], (optional)
               @replace_sel (bool): Replace the current selection
                  (optional)
               @overlap (bool): Don't correct overlap on new sequence strips
                  (optional)
               @scene (str): in [], (optional)

            '''

            pass

        def select(extend=False, linked_handle=False, left_right='NONE', linked_time=False):
            '''Select a strip (last selected becomes the "active strip")
               Arguments:
               @extend (bool): Extend the selection
                  (optional)
               @linked_handle (bool): Select handles next to the active strip
                  (optional)
               @left_right (str): Select based on the current frame side the cursor is on
                  in ['NONE', 'MOUSE', 'LEFT', 'RIGHT'], (optional)
               @linked_time (bool): Select other strips at the same time
                  (optional)

            '''

            pass

        def select_active_side(side='BOTH'):
            '''Select strips on the nominated side of the active strip
               Arguments:
               @side (str): The side of the handle that is selected
                  in ['LEFT', 'RIGHT', 'BOTH'], (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''Select or deselect all strips
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select strips using border selection
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_grouped(type='TYPE', extend=False, use_active_channel=False):
            '''Select all strips grouped by various properties
               Arguments:
               @type (str): in ['TYPE', 'TYPE_BASIC', 'TYPE_EFFECT', 'DATA', 'EFFECT', 'EFFECT_LINK', 'OVERLAP'], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @use_active_channel (bool): Only consider strips on the same channel as the active one
                  (optional)

            '''

            pass

        def select_handles(side='BOTH'):
            '''Select manipulator handles on the sides of the selected strip
               Arguments:
               @side (str): The side of the handle that is selected
                  in ['LEFT', 'RIGHT', 'BOTH'], (optional)

            '''

            pass

        def select_less():
            '''Shrink the current selection of adjacent selected strips
            '''

            pass

        def select_linked():
            '''Select all strips adjacent to the current selection
            '''

            pass

        def select_linked_pick(extend=False):
            '''Select a chain of linked strips nearest to the mouse pointer
               Arguments:
               @extend (bool): Extend the selection
                  (optional)

            '''

            pass

        def select_more():
            '''Select more strips adjacent to the current selection
            '''

            pass

        def slip(offset=0):
            '''Trim the contents of the active strip
               Arguments:
               @offset (int): Offset to the data of the strip
                  in [-inf, inf], (optional)

            '''

            pass

        def snap(frame=0):
            '''Frame where selected strips will be snapped
               Arguments:
               @frame (int): Frame where selected strips will be snapped
                  in [-inf, inf], (optional)

            '''

            pass

        def sound_strip_add(filepath="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, channel=1, replace_sel=True, overlap=False, cache=False, mono=False):
            '''Add a sound strip to the sequencer
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @frame_start (int): Start frame of the sequence strip
                  in [-inf, inf], (optional)
               @channel (int): Channel to place this strip into
                  in [1, 32], (optional)
               @replace_sel (bool): Replace the current selection
                  (optional)
               @overlap (bool): Don't correct overlap on new sequence strips
                  (optional)
               @cache (bool): Cache the sound in memory
                  (optional)
               @mono (bool): Merge all the sound's channels into one
                  (optional)

            '''

            pass

        def strip_jump(next=True, center=True):
            '''Move frame to previous edit point
               Arguments:
               @next (bool): (optional)
               @center (bool): (optional)

            '''

            pass

        def strip_modifier_add(type='COLOR_BALANCE'):
            '''Add a modifier to the strip
               Arguments:
               @type (str): in ['COLOR_BALANCE', 'CURVES', 'HUE_CORRECT', 'BRIGHT_CONTRAST', 'MASK', 'WHITE_BALANCE', 'TONEMAP'], (optional)

            '''

            pass

        def strip_modifier_copy(type='REPLACE'):
            '''Copy modifiers of the active strip to all selected strips
               Arguments:
               @type (str): in ['REPLACE', 'APPEND'], (optional)

            '''

            pass

        def strip_modifier_move(name="Name", direction='UP'):
            '''Move modifier up and down in the stack
               Arguments:
               @name (str): Name of modifier to remove
                  (optional, never None)
               @direction (str): in ['UP', 'DOWN'], (optional)

            '''

            pass

        def strip_modifier_remove(name="Name"):
            '''Remove a modifier from the strip
               Arguments:
               @name (str): Name of modifier to remove
                  (optional, never None)

            '''

            pass

        def swap(side='RIGHT'):
            '''Swap active strip with strip to the right or left
               Arguments:
               @side (str): Side of the strip to swap
                  in ['LEFT', 'RIGHT'], (optional)

            '''

            pass

        def swap_data():
            '''Swap 2 sequencer strips
            '''

            pass

        def swap_inputs():
            '''Swap the first two inputs for the effect strip
            '''

            pass

        def unlock():
            '''Unlock the active strip so that it can't be transformed
            '''

            pass

        def unmute(unselected=False):
            '''Unmute (un)selected strips
               Arguments:
               @unselected (bool): Unmute unselected rather than selected strips
                  (optional)

            '''

            pass

        def view_all():
            '''View all the strips in the sequencer
            '''

            pass

        def view_all_preview():
            '''Zoom preview to fit in the area
            '''

            pass

        def view_frame():
            '''Reset viewable area to show range around current frame
            '''

            pass

        def view_ghost_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
            '''Set the boundaries of the border used for offset-view
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def view_selected():
            '''Zoom the sequencer on the selected strips
            '''

            pass

        def view_toggle():
            '''Toggle between sequencer views (sequence, preview, both)
            '''

            pass

        def view_zoom_ratio(ratio=1.0):
            '''Change zoom ratio of sequencer preview
               Arguments:
               @ratio (float): Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
                  in [-inf, inf], (optional)

            '''

            pass

    class sketch:
        '''Spcecial class, created just to reflect content of bpy.ops.sketch'''

        def cancel_stroke():
            '''Cancel the current sketch stroke
            '''

            pass

        def convert():
            '''Convert the selected sketch strokes to bone chains
            '''

            pass

        def delete():
            '''Delete a sketch stroke
            '''

            pass

        def draw_preview(snap=False):
            '''Draw preview of current sketch stroke (internal use)
               Arguments:
               @snap (bool): (optional)

            '''

            pass

        def draw_stroke(snap=False):
            '''Start to draw a sketch stroke
               Arguments:
               @snap (bool): (optional)

            '''

            pass

        def finish_stroke():
            '''End and keep the current sketch stroke
            '''

            pass

        def gesture(snap=False):
            '''Start to draw a gesture stroke
               Arguments:
               @snap (bool): (optional)

            '''

            pass

        def select():
            '''Select a sketch stroke
            '''

            pass

    class sound:
        '''Spcecial class, created just to reflect content of bpy.ops.sound'''

        def bake_animation():
            '''Update the audio animation cache
            '''

            pass

        def mixdown(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', accuracy=1024, container='FLAC', codec='FLAC', format='S16', bitrate=192, split_channels=False):
            '''Mixes the scene's audio to a sound file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @accuracy (int): Sample accuracy, important for animation data (the lower the value, the more accurate)
                  in [1, inf], (optional)
               @container (str): File format
                  in ['AC3', 'FLAC', 'MATROSKA', 'MP2', 'MP3', 'OGG', 'WAV'], (optional)
               @codec (str): Audio Codec
                  in ['AAC', 'AC3', 'FLAC', 'MP2', 'MP3', 'PCM', 'VORBIS'], (optional)
               @format (str): Sample format
                  in ['U8', 'S16', 'S24', 'S32', 'F32', 'F64'], (optional)
               @bitrate (int): Bitrate in kbit/s
                  in [32, 512], (optional)
               @split_channels (bool): Each channel will be rendered into a mono file
                  (optional)

            '''

            pass

        def open(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', cache=False, mono=False):
            '''Load a sound file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @cache (bool): Cache the sound in memory
                  (optional)
               @mono (bool): Merge all the sound's channels into one
                  (optional)

            '''

            pass

        def open_mono(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', cache=False, mono=True):
            '''Load a sound file as mono
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @cache (bool): Cache the sound in memory
                  (optional)
               @mono (bool): Mixdown the sound to mono
                  (optional)

            '''

            pass

        def pack():
            '''Pack the sound into the current blend file
            '''

            pass

        def unpack(method='USE_LOCAL', id=""):
            '''Unpack the sound to the samples filename
               Arguments:
               @method (str): How to unpack
                  in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)
               @id (str): Sound datablock name to unpack
                  (optional, never None)

            '''

            pass

        def update_animation_flags():
            '''Update animation flags
            '''

            pass

    class surface:
        '''Spcecial class, created just to reflect content of bpy.ops.surface'''

        def primitive_nurbs_surface_circle_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Nurbs surface Circle
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_nurbs_surface_curve_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Nurbs surface Curve
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_nurbs_surface_cylinder_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Nurbs surface Cylinder
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_nurbs_surface_sphere_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Nurbs surface Sphere
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_nurbs_surface_surface_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Nurbs surface Patch
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

        def primitive_nurbs_surface_torus_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
            '''Construct a Nurbs surface Torus
               Arguments:
               @radius (float): in [0, inf], (optional)
               @view_align (bool): Align the new object to the view
                  (optional)
               @enter_editmode (bool): Enter editmode when adding this object
                  (optional)
               @location (float): Location for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @rotation (float): Rotation for the newly added object
                  array of 3 items in [-inf, inf], (optional)
               @layers (bool): array of 20 items, (optional)

            '''

            pass

    class text:
        '''Spcecial class, created just to reflect content of bpy.ops.text'''

        def autocomplete():
            '''Show a list of used text in the open document
            '''

            pass

        def comment():
            '''Convert selected text to comment
            '''

            pass

        def convert_whitespace(type='SPACES'):
            '''Convert whitespaces by type
               Arguments:
               @type (str): Type of whitespace to convert to
                  in ['SPACES', 'TABS'], (optional)

            '''

            pass

        def copy():
            '''Copy selected text to clipboard
            '''

            pass

        def cursor_set(x=0, y=0):
            '''Set cursor position
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)

            '''

            pass

        def cut():
            '''Cut selected text to clipboard
            '''

            pass

        def delete(type='NEXT_CHARACTER'):
            '''Delete text by cursor position
               Arguments:
               @type (str): Which part of the text to delete
                  in ['NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'NEXT_WORD', 'PREVIOUS_WORD'], (optional)

            '''

            pass

        def duplicate_line():
            '''Duplicate the current line
            '''

            pass

        def find():
            '''Find specified text
            '''

            pass

        def find_set_selected():
            '''Find specified text and set as selected
            '''

            pass

        def indent():
            '''Indent selected text
            '''

            pass

        def insert(text=""):
            '''Insert text at cursor position
               Arguments:
               @text (str): Text to insert at the cursor position
                  (optional, never None)

            '''

            pass

        def jump(line=1):
            '''Jump cursor to line
               Arguments:
               @line (int): Line number to jump to
                  in [1, inf], (optional)

            '''

            pass

        def line_break():
            '''Insert line break at cursor position
            '''

            pass

        def line_number():
            '''The current line number
            '''

            pass

        def make_internal():
            '''Make active text file internal
            '''

            pass

        def move(type='LINE_BEGIN'):
            '''Move cursor to position type
               Arguments:
               @type (str): Where to move cursor to
                  in ['LINE_BEGIN', 'LINE_END', 'FILE_TOP', 'FILE_BOTTOM', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)

            '''

            pass

        def move_lines(direction='DOWN'):
            '''Move the currently selected line(s) up/down
               Arguments:
               @direction (str): in ['UP', 'DOWN'], (optional)

            '''

            pass

        def move_select(type='LINE_BEGIN'):
            '''Move the cursor while selecting
               Arguments:
               @type (str): Where to move cursor to, to make a selection
                  in ['LINE_BEGIN', 'LINE_END', 'FILE_TOP', 'FILE_BOTTOM', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)

            '''

            pass

        def new():
            '''Create a new text data block
            '''

            pass

        def open(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=True, filter_font=False, filter_sound=False, filter_text=True, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', internal=False):
            '''Open a new text data block
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @internal (bool): Make text file internal after loading
                  (optional)

            '''

            pass

        def overwrite_toggle():
            '''Toggle overwrite while typing
            '''

            pass

        def paste(selection=False):
            '''Paste text from clipboard
               Arguments:
               @selection (bool): Paste text selected elsewhere rather than copied (X11 only)
                  (optional)

            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def refresh_pyconstraints():
            '''Refresh all pyconstraints
            '''

            pass

        def reload():
            '''Reload active text data block from its file
            '''

            pass

        def replace():
            '''Replace text with the specified text
            '''

            pass

        def replace_set_selected():
            '''Replace text with specified text and set as selected
            '''

            pass

        def resolve_conflict(resolution='IGNORE'):
            '''When external text is out of sync, resolve the conflict
               Arguments:
               @resolution (str): How to solve conflict due to differences in internal and external text
                  in ['IGNORE', 'RELOAD', 'SAVE', 'MAKE_INTERNAL'], (optional)

            '''

            pass

        def run_script():
            '''Run active script
            '''

            pass

        def save():
            '''Save active text data block
            '''

            pass

        def save_as(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=True, filter_font=False, filter_sound=False, filter_text=True, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Save active text file with options
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def scroll(lines=1):
            '''undocumented
               Arguments:
               @lines (int): Number of lines to scroll
                  in [-inf, inf], (optional)

            '''

            pass

        def scroll_bar(lines=1):
            '''undocumented
               Arguments:
               @lines (int): Number of lines to scroll
                  in [-inf, inf], (optional)

            '''

            pass

        def select_all():
            '''Select all text
            '''

            pass

        def select_line():
            '''Select text by line
            '''

            pass

        def select_word():
            '''Select word under cursor
            '''

            pass

        def selection_set(select=False):
            '''Set cursor selection
               Arguments:
               @select (bool): Set selection end rather than cursor
                  (optional)

            '''

            pass

        def start_find():
            '''Start searching text
            '''

            pass

        def to_3d_object(split_lines=False):
            '''Create 3D text object from active text data block
               Arguments:
               @split_lines (bool): Create one object per line in the text
                  (optional)

            '''

            pass

        def uncomment():
            '''Convert selected comment to text
            '''

            pass

        def unindent():
            '''Unindent selected text
            '''

            pass

        def unlink():
            '''Unlink active text data block
            '''

            pass

    class texture:
        '''Spcecial class, created just to reflect content of bpy.ops.texture'''

        def envmap_clear():
            '''Discard the environment map and free it from memory
            '''

            pass

        def envmap_clear_all():
            '''Discard all environment maps in the .blend file and free them from memory
            '''

            pass

        def envmap_save(layout=(0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 1.0), filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Save the current generated Environment map to an image file
               Arguments:
               @layout (float): Flat array describing the X,Y position of each cube face in the output image, where 1 is the size of a face - order is [+Z -Z +Y -X -Y +X] (use -1 to skip a face)
                  array of 12 items in [-inf, inf], (optional)
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def new():
            '''Add a new texture
            '''

            pass

        def slot_copy():
            '''Copy the material texture settings and nodes
            '''

            pass

        def slot_move(type='UP'):
            '''Move texture slots up and down
               Arguments:
               @type (str): in ['UP', 'DOWN'], (optional)

            '''

            pass

        def slot_paste():
            '''Copy the texture settings and nodes
            '''

            pass

    class time:
        '''Spcecial class, created just to reflect content of bpy.ops.time'''

        def end_frame_set():
            '''Set the end frame
            '''

            pass

        def start_frame_set():
            '''Set the start frame
            '''

            pass

        def view_all():
            '''Show the entire playable frame range
            '''

            pass

        def view_frame():
            '''Reset viewable area to show range around current frame
            '''

            pass

    class transform:
        '''Spcecial class, created just to reflect content of bpy.ops.transform'''

        def bend(value=(0.0), mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False):
            '''Bend selected items between the 3D cursor and the mouse
               Arguments:
               @value (float): array of 1 items in [-inf, inf], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def create_orientation(name="", use_view=False, use=False, overwrite=False):
            '''Create transformation orientation from selection
               Arguments:
               @name (str): Name of the new custom orientation
                  (optional, never None)
               @use_view (bool): Use the current view instead of the active object to create the new orientation
                  (optional)
               @use (bool): Select orientation after its creation
                  (optional)
               @overwrite (bool): Overwrite previously created orientation with same name
                  (optional)

            '''

            pass

        def delete_orientation():
            '''Delete transformation orientation
            '''

            pass

        def edge_bevelweight(value=0.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False):
            '''Change the bevel weight of edges
               Arguments:
               @value (float): in [-1, 1], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def edge_crease(value=0.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False):
            '''Change the crease of edges
               Arguments:
               @value (float): in [-1, 1], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def edge_slide(value=0.0, single_side=False, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), correct_uv=False, release_confirm=False):
            '''Slide an edge loop along a mesh
               Arguments:
               @value (float): in [-10, 10], (optional)
               @single_side (bool): (optional)
               @use_even (bool): Make the edge loop match the shape of the adjacent edge loop
                  (optional)
               @flipped (bool): When Even mode is active, flips between the two adjacent edge loops
                  (optional)
               @use_clamp (bool): Clamp within the edge extents
                  (optional)
               @mirror (bool): (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @correct_uv (bool): Correct UV coordinates when transforming
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def mirror(constraint_axis=(False, False, False), constraint_orientation='GLOBAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, gpencil_strokes=False, release_confirm=False):
            '''Mirror selected items around one or more axes
               Arguments:
               @constraint_axis (bool): array of 3 items, (optional)
               @constraint_orientation (str): Transformation orientation
                  in [], (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def push_pull(value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False):
            '''Push/Pull selected items
               Arguments:
               @value (float): in [-inf, inf], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def resize(value=(1.0, 1.0, 1.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False):
            '''Scale (resize) selected items
               Arguments:
               @value (float): array of 3 items in [-inf, inf], (optional)
               @constraint_axis (bool): array of 3 items, (optional)
               @constraint_orientation (str): Transformation orientation
                  in [], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @texture_space (bool): Edit Object data texture space
                  (optional)
               @remove_on_cancel (bool): Remove elements on cancel
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def rotate(value=0.0, axis=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False):
            '''Rotate selected items
               Arguments:
               @value (float): in [-inf, inf], (optional)
               @axis (float): The axis around which the transformation occurs
                  array of 3 items in [-inf, inf], (optional)
               @constraint_axis (bool): array of 3 items, (optional)
               @constraint_orientation (str): Transformation orientation
                  in [], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def select_orientation(orientation='GLOBAL'):
            '''Select transformation orientation
               Arguments:
               @orientation (str): Transformation orientation
                  in [], (optional)

            '''

            pass

        def seq_slide(value=(0.0, 0.0), snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False):
            '''Slide a sequence strip in time
               Arguments:
               @value (float): array of 2 items in [-inf, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def shear(value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False):
            '''Shear selected items along the horizontal screen axis
               Arguments:
               @value (float): in [-inf, inf], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def shrink_fatten(value=0.0, use_even_offset=True, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False):
            '''Shrink/fatten selected vertices along normals
               Arguments:
               @value (float): in [-inf, inf], (optional)
               @use_even_offset (bool): Scale the offset to give more even thickness
                  (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def skin_resize(value=(1.0, 1.0, 1.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False):
            '''Scale selected vertices' skin radii
               Arguments:
               @value (float): array of 3 items in [-inf, inf], (optional)
               @constraint_axis (bool): array of 3 items, (optional)
               @constraint_orientation (str): Transformation orientation
                  in [], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def tilt(value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False):
            '''Tilt selected control vertices of 3D curve
               Arguments:
               @value (float): in [-inf, inf], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def tosphere(value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False):
            '''Move selected vertices outward in a spherical shape around mesh center
               Arguments:
               @value (float): in [0, 1], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def trackball(value=(0.0, 0.0), mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False):
            '''Trackball style rotation of selected items
               Arguments:
               @value (float): array of 2 items in [-inf, inf], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def transform(mode='TRANSLATION', value=(0.0, 0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False):
            '''Transform selected items by mode type
               Arguments:
               @mode (str): in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)
               @value (float): array of 4 items in [-inf, inf], (optional)
               @axis (float): The axis around which the transformation occurs
                  array of 3 items in [-inf, inf], (optional)
               @constraint_axis (bool): array of 3 items, (optional)
               @constraint_orientation (str): Transformation orientation
                  in [], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def translate(value=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False):
            '''Translate (move) selected items
               Arguments:
               @value (float): array of 3 items in [-inf, inf], (optional)
               @constraint_axis (bool): array of 3 items, (optional)
               @constraint_orientation (str): Transformation orientation
                  in [], (optional)
               @mirror (bool): (optional)
               @proportional (str): in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
               @proportional_edit_falloff (str): Falloff type for proportional editing mode
                  in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
               @proportional_size (float): in [1e-06, inf], (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @gpencil_strokes (bool): Edit selected Grease Pencil strokes
                  (optional)
               @texture_space (bool): Edit Object data texture space
                  (optional)
               @remove_on_cancel (bool): Remove elements on cancel
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def vert_slide(value=0.0, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), correct_uv=False, release_confirm=False):
            '''Slide a vertex along a mesh
               Arguments:
               @value (float): in [-10, 10], (optional)
               @use_even (bool): Make the edge loop match the shape of the adjacent edge loop
                  (optional)
               @flipped (bool): When Even mode is active, flips between the two adjacent edge loops
                  (optional)
               @use_clamp (bool): Clamp within the edge extents
                  (optional)
               @mirror (bool): (optional)
               @snap (bool): (optional)
               @snap_target (str): in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
               @snap_point (float): array of 3 items in [-inf, inf], (optional)
               @snap_align (bool): (optional)
               @snap_normal (float): array of 3 items in [-inf, inf], (optional)
               @correct_uv (bool): Correct UV coordinates when transforming
                  (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def vertex_random(offset=0.1, uniform=0.0, normal=0.0, seed=0):
            '''Randomize vertices
               Arguments:
               @offset (float): Distance to offset
                  in [-inf, inf], (optional)
               @uniform (float): Increase for uniform offset distance
                  in [0, 1], (optional)
               @normal (float): Align offset direction to normals
                  in [0, 1], (optional)
               @seed (int): Seed for the random number generator
                  in [0, 10000], (optional)

            '''

            pass

        def vertex_warp(warp_angle=6.28319, offset_angle=0.0, min=-1, max=1.0, viewmat=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), center=(0.0, 0.0, 0.0)):
            '''Warp vertices around the cursor
               Arguments:
               @warp_angle (float): Amount to warp about the cursor
                  in [-inf, inf], (optional)
               @offset_angle (float): Angle to use as the basis for warping
                  in [-inf, inf], (optional)
               @min (float): in [-inf, inf], (optional)
               @max (float): in [-inf, inf], (optional)
               @viewmat (float): array of 16 items in [-inf, inf], (optional)
               @center (float): array of 3 items in [-inf, inf], (optional)

            '''

            pass

    class ui:
        '''Spcecial class, created just to reflect content of bpy.ops.ui'''

        def copy_data_path_button():
            '''Copy the RNA data path for this property to the clipboard
            '''

            pass

        def copy_python_command_button():
            '''Copy the Python command matching this button
            '''

            pass

        def copy_to_selected_button(all=True):
            '''Copy property from this object to selected objects or bones
               Arguments:
               @all (bool): Copy to selected all elements of the array
                  (optional)

            '''

            pass

        def drop_color(color=(0.0, 0.0, 0.0), gamma=False):
            '''Drop colors to buttons
               Arguments:
               @color (float): Source color
                  array of 3 items in [0, inf], (optional)
               @gamma (bool): The source color is gamma corrected
                  (optional)

            '''

            pass

        def editsource():
            '''Edit UI source code of the active button
            '''

            pass

        def edittranslation_init():
            '''Edit i18n in current language for the active button
            '''

            pass

        def eyedropper_color():
            '''Sample a color from the Blender Window to store in a property
            '''

            pass

        def eyedropper_depth():
            '''Sample depth from the 3D view
            '''

            pass

        def eyedropper_driver(mapping_type='SINGLE_MANY'):
            '''Pick a property to use as a driver target
               Arguments:
               @mapping_type (str): Method used to match target and driven properties
                  in ['SINGLE_MANY', 'DIRECT', 'MATCH', 'NONE_ALL', 'NONE_SINGLE'], (optional)

            '''

            pass

        def eyedropper_id():
            '''Sample a datablock from the 3D View to store in a property
            '''

            pass

        def reloadtranslation():
            '''Force a full reload of UI translation
            '''

            pass

        def reports_to_textblock():
            '''Write the reports
            '''

            pass

        def reset_default_button(all=True):
            '''Reset this property's value to its default value
               Arguments:
               @all (bool): Reset to default values all elements of the array
                  (optional)

            '''

            pass

        def reset_default_theme():
            '''Reset to the default theme colors
            '''

            pass

        def unset_property_button():
            '''Clear the property and use default or generated value in operators
            '''

            pass

    class uv:
        '''Spcecial class, created just to reflect content of bpy.ops.uv'''

        def align(axis='ALIGN_AUTO'):
            '''Align selected UV vertices to an axis
               Arguments:
               @axis (str): Axis to align UV locations on
                  in ['ALIGN_S', 'ALIGN_T', 'ALIGN_U', 'ALIGN_AUTO', 'ALIGN_X', 'ALIGN_Y'], (optional)

            '''

            pass

        def average_islands_scale():
            '''Average the size of separate UV islands, based on their area in 3D space
            '''

            pass

        def circle_select(x=0, y=0, radius=1, gesture_mode=0):
            '''Select UV vertices using circle selection
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @radius (int): in [1, inf], (optional)
               @gesture_mode (int): in [-inf, inf], (optional)

            '''

            pass

        def cube_project(cube_size=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
            '''Project the UV vertices of the mesh over the six faces of a cube
               Arguments:
               @cube_size (float): Size of the cube to project on
                  in [0, inf], (optional)
               @correct_aspect (bool): Map UVs taking image aspect ratio into account
                  (optional)
               @clip_to_bounds (bool): Clip UV coordinates to bounds after unwrapping
                  (optional)
               @scale_to_bounds (bool): Scale UV coordinates to bounds after unwrapping
                  (optional)

            '''

            pass

        def cursor_set(location=(0.0, 0.0)):
            '''Set 2D cursor location
               Arguments:
               @location (float): Cursor location in normalized (0.0-1.0) coordinates
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def cylinder_project(direction='VIEW_ON_EQUATOR', align='POLAR_ZX', radius=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
            '''Project the UV vertices of the mesh over the curved wall of a cylinder
               Arguments:
               @direction (str): Direction of the sphere or cylinder
                  in ['VIEW_ON_EQUATOR', 'VIEW_ON_POLES', 'ALIGN_TO_OBJECT'], (optional)
               @align (str): How to determine rotation around the pole
                  in ['POLAR_ZX', 'POLAR_ZY'], (optional)
               @radius (float): Radius of the sphere or cylinder
                  in [0, inf], (optional)
               @correct_aspect (bool): Map UVs taking image aspect ratio into account
                  (optional)
               @clip_to_bounds (bool): Clip UV coordinates to bounds after unwrapping
                  (optional)
               @scale_to_bounds (bool): Scale UV coordinates to bounds after unwrapping
                  (optional)

            '''

            pass

        def export_layout(filepath="", check_existing=True, export_all=False, modified=False, mode='PNG', size=(1024, 1024), opacity=0.25, tessellated=False):
            '''Export UV layout to file
               Arguments:
               @filepath (str): (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @export_all (bool): Export all UVs in this mesh (not just visible ones)
                  (optional)
               @modified (bool): Exports UVs from the modified mesh
                  (optional)
               @mode (str): File format to export the UV layout to
                  in ['SVG', 'EPS', 'PNG'], (optional)
               @size (int): Dimensions of the exported file
                  array of 2 items in [8, 32768], (optional)
               @opacity (float): Set amount of opacity for exported UV layout
                  in [0, 1], (optional)
               @tessellated (bool): Export tessellated UVs instead of polygons ones
                  (optional)

            '''

            pass

        def follow_active_quads(mode='LENGTH_AVERAGE'):
            '''Follow UVs from active quads along continuous face loops
               Arguments:
               @mode (str): Method to space UV edge loops
                  in ['EVEN', 'LENGTH', 'LENGTH_AVERAGE'], (optional)

            '''

            pass

        def hide(unselected=False):
            '''Hide (un)selected UV vertices
               Arguments:
               @unselected (bool): Hide unselected rather than selected
                  (optional)

            '''

            pass

        def lightmap_pack(PREF_CONTEXT='SEL_FACES', PREF_PACK_IN_ONE=True, PREF_NEW_UVLAYER=False, PREF_APPLY_IMAGE=False, PREF_IMG_PX_SIZE=512, PREF_BOX_DIV=12, PREF_MARGIN_DIV=0.1):
            '''Pack each faces UV's into the UV bounds
               Arguments:
               @PREF_CONTEXT (str): in ['SEL_FACES', 'ALL_FACES', 'ALL_OBJECTS'], (optional)
               @PREF_PACK_IN_ONE (bool): Objects Share texture space, map all objects into 1 uvmap
                  (optional)
               @PREF_NEW_UVLAYER (bool): Create a new UV map for every mesh packed
                  (optional)
               @PREF_APPLY_IMAGE (bool): Assign new images for every mesh (only one if shared tex space enabled)
                  (optional)
               @PREF_IMG_PX_SIZE (int): Width and Height for the new image
                  in [64, 5000], (optional)
               @PREF_BOX_DIV (int): Pre Packing before the complex boxpack
                  in [1, 48], (optional)
               @PREF_MARGIN_DIV (float): Size of the margin as a division of the UV
                  in [0.001, 1], (optional)

            '''

            pass

        def mark_seam(clear=False):
            '''Mark selected UV edges as seams
               Arguments:
               @clear (bool): Clear instead of marking seams
                  (optional)

            '''

            pass

        def minimize_stretch(fill_holes=True, blend=0.0, iterations=0):
            '''Reduce UV stretching by relaxing angles
               Arguments:
               @fill_holes (bool): Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
                  (optional)
               @blend (float): Blend factor between stretch minimized and original
                  in [0, 1], (optional)
               @iterations (int): Number of iterations to run, 0 is unlimited when run interactively
                  in [0, inf], (optional)

            '''

            pass

        def pack_islands(rotate=True, margin=0.001):
            '''Transform all islands so that they fill up the UV space as much as possible
               Arguments:
               @rotate (bool): Rotate islands for best fit
                  (optional)
               @margin (float): Space between islands
                  in [0, 1], (optional)

            '''

            pass

        def pin(clear=False):
            '''Set/clear selected UV vertices as anchored between multiple unwrap operations
               Arguments:
               @clear (bool): Clear pinning for the selection instead of setting it
                  (optional)

            '''

            pass

        def project_from_view(orthographic=False, camera_bounds=True, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
            '''Project the UV vertices of the mesh as seen in current 3D view
               Arguments:
               @orthographic (bool): Use orthographic projection
                  (optional)
               @camera_bounds (bool): Map UVs to the camera region taking resolution and aspect into account
                  (optional)
               @correct_aspect (bool): Map UVs taking image aspect ratio into account
                  (optional)
               @clip_to_bounds (bool): Clip UV coordinates to bounds after unwrapping
                  (optional)
               @scale_to_bounds (bool): Scale UV coordinates to bounds after unwrapping
                  (optional)

            '''

            pass

        def remove_doubles(threshold=0.02, use_unselected=False):
            '''Selected UV vertices that are within a radius of each other are welded together
               Arguments:
               @threshold (float): Maximum distance between welded vertices
                  in [0, 10], (optional)
               @use_unselected (bool): Merge selected to other unselected vertices
                  (optional)

            '''

            pass

        def reset():
            '''Reset UV projection
            '''

            pass

        def reveal():
            '''Reveal all hidden UV vertices
            '''

            pass

        def seams_from_islands(mark_seams=True, mark_sharp=False):
            '''Set mesh seams according to island setup in the UV editor
               Arguments:
               @mark_seams (bool): Mark boundary edges as seams
                  (optional)
               @mark_sharp (bool): Mark boundary edges as sharp
                  (optional)

            '''

            pass

        def select(extend=False, location=(0.0, 0.0)):
            '''Select UV vertices
               Arguments:
               @extend (bool): Extend selection rather than clearing the existing selection
                  (optional)
               @location (float): Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def select_all(action='TOGGLE'):
            '''Change selection of all UV vertices
               Arguments:
               @action (str): Selection action to execute
                  in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

            '''

            pass

        def select_border(pinned=False, gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select UV vertices using border selection
               Arguments:
               @pinned (bool): Border select pinned UVs only
                  (optional)
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_lasso(path=None, deselect=False, extend=True):
            '''Select UVs using lasso selection
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @deselect (bool): Deselect rather than select items
                  (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_less():
            '''Deselect UV vertices at the boundary of each selection region
            '''

            pass

        def select_linked(extend=False):
            '''Select all UV vertices linked to the active UV map
               Arguments:
               @extend (bool): Extend selection rather than clearing the existing selection
                  (optional)

            '''

            pass

        def select_linked_pick(extend=False, location=(0.0, 0.0)):
            '''Select all UV vertices linked under the mouse
               Arguments:
               @extend (bool): Extend selection rather than clearing the existing selection
                  (optional)
               @location (float): Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def select_loop(extend=False, location=(0.0, 0.0)):
            '''Select a loop of connected UV vertices
               Arguments:
               @extend (bool): Extend selection rather than clearing the existing selection
                  (optional)
               @location (float): Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def select_more():
            '''Select more UV vertices connected to initial selection
            '''

            pass

        def select_pinned():
            '''Select all pinned UV vertices
            '''

            pass

        def select_split():
            '''Select only entirely selected faces
            '''

            pass

        def smart_project(angle_limit=66.0, island_margin=0.0, user_area_weight=0.0, use_aspect=True, stretch_to_bounds=True):
            '''This script projection unwraps the selected faces of a mesh (it operates on all selected mesh objects, and can be used to unwrap selected faces, or all faces)
               Arguments:
               @angle_limit (float): Lower for more projection groups, higher for less distortion
                  in [1, 89], (optional)
               @island_margin (float): Margin to reduce bleed from adjacent islands
                  in [0, 1], (optional)
               @user_area_weight (float): Weight projections vector by faces with larger areas
                  in [0, 1], (optional)
               @use_aspect (bool): Map UVs taking image aspect ratio into account
                  (optional)
               @stretch_to_bounds (bool): Stretch the final output to texture bounds
                  (optional)

            '''

            pass

        def snap_cursor(target='PIXELS'):
            '''Snap cursor to target type
               Arguments:
               @target (str): Target to snap the selected UVs to
                  in ['PIXELS', 'SELECTED'], (optional)

            '''

            pass

        def snap_selected(target='PIXELS'):
            '''Snap selected UV vertices to target type
               Arguments:
               @target (str): Target to snap the selected UVs to
                  in ['PIXELS', 'CURSOR', 'CURSOR_OFFSET', 'ADJACENT_UNSELECTED'], (optional)

            '''

            pass

        def sphere_project(direction='VIEW_ON_EQUATOR', align='POLAR_ZX', correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
            '''Project the UV vertices of the mesh over the curved surface of a sphere
               Arguments:
               @direction (str): Direction of the sphere or cylinder
                  in ['VIEW_ON_EQUATOR', 'VIEW_ON_POLES', 'ALIGN_TO_OBJECT'], (optional)
               @align (str): How to determine rotation around the pole
                  in ['POLAR_ZX', 'POLAR_ZY'], (optional)
               @correct_aspect (bool): Map UVs taking image aspect ratio into account
                  (optional)
               @clip_to_bounds (bool): Clip UV coordinates to bounds after unwrapping
                  (optional)
               @scale_to_bounds (bool): Scale UV coordinates to bounds after unwrapping
                  (optional)

            '''

            pass

        def stitch(use_limit=False, snap_islands=True, limit=0.01, static_island=0, midpoint_snap=False, clear_seams=True, mode='VERTEX', stored_mode='VERTEX', selection=None):
            '''Stitch selected UV vertices by proximity
               Arguments:
               @use_limit (bool): Stitch UVs within a specified limit distance
                  (optional)
               @snap_islands (bool): Snap islands together (on edge stitch mode, rotates the islands too)
                  (optional)
               @limit (float): Limit distance in normalized coordinates
                  in [0, inf], (optional)
               @static_island (int): Island that stays in place when stitching islands
                  in [0, inf], (optional)
               @midpoint_snap (bool): UVs are stitched at midpoint instead of at static island
                  (optional)
               @clear_seams (bool): Clear seams of stitched edges
                  (optional)
               @mode (str): Use vertex or edge stitching
                  in ['VERTEX', 'EDGE'], (optional)
               @stored_mode (str): Use vertex or edge stitching
                  in ['VERTEX', 'EDGE'], (optional)
               @selection (SelectedUvElement): Collection of , (optional)

            '''

            pass

        def tile_set(tile=(0, 0)):
            '''Set UV image tile coordinates
               Arguments:
               @tile (int): Tile coordinate
                  array of 2 items in [0, inf], (optional)

            '''

            pass

        def unwrap(method='ANGLE_BASED', fill_holes=True, correct_aspect=True, use_subsurf_data=False, margin=0.001):
            '''Unwrap the mesh of the object being edited
               Arguments:
               @method (str): Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
                  in ['ANGLE_BASED', 'CONFORMAL'], (optional)
               @fill_holes (bool): Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
                  (optional)
               @correct_aspect (bool): Map UVs taking image aspect ratio into account
                  (optional)
               @use_subsurf_data (bool): Map UVs taking vertex position after subsurf into account
                  (optional)
               @margin (float): Space between islands
                  in [0, 1], (optional)

            '''

            pass

        def weld():
            '''Weld selected UV vertices together
            '''

            pass

    class view2d:
        '''Spcecial class, created just to reflect content of bpy.ops.view2d'''

        def ndof():
            '''Use a 3D mouse device to pan/zoom the view
            '''

            pass

        def pan(deltax=0, deltay=0):
            '''Pan the view
               Arguments:
               @deltax (int): in [-inf, inf], (optional)
               @deltay (int): in [-inf, inf], (optional)

            '''

            pass

        def reset():
            '''Reset the view
            '''

            pass

        def scroll_down(deltax=0, deltay=0, page=False):
            '''Scroll the view down
               Arguments:
               @deltax (int): in [-inf, inf], (optional)
               @deltay (int): in [-inf, inf], (optional)
               @page (bool): Scroll down one page
                  (optional)

            '''

            pass

        def scroll_left(deltax=0, deltay=0):
            '''Scroll the view left
               Arguments:
               @deltax (int): in [-inf, inf], (optional)
               @deltay (int): in [-inf, inf], (optional)

            '''

            pass

        def scroll_right(deltax=0, deltay=0):
            '''Scroll the view right
               Arguments:
               @deltax (int): in [-inf, inf], (optional)
               @deltay (int): in [-inf, inf], (optional)

            '''

            pass

        def scroll_up(deltax=0, deltay=0, page=False):
            '''Scroll the view up
               Arguments:
               @deltax (int): in [-inf, inf], (optional)
               @deltay (int): in [-inf, inf], (optional)
               @page (bool): Scroll up one page
                  (optional)

            '''

            pass

        def scroller_activate():
            '''Scroll view by mouse click and drag
            '''

            pass

        def smoothview(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
            '''undocumented
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def zoom(deltax=0.0, deltay=0.0):
            '''Zoom in/out the view
               Arguments:
               @deltax (float): in [-inf, inf], (optional)
               @deltay (float): in [-inf, inf], (optional)

            '''

            pass

        def zoom_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
            '''Zoom in the view to the nearest item contained in the border
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def zoom_in(zoomfacx=0.0, zoomfacy=0.0):
            '''Zoom in the view
               Arguments:
               @zoomfacx (float): in [-inf, inf], (optional)
               @zoomfacy (float): in [-inf, inf], (optional)

            '''

            pass

        def zoom_out(zoomfacx=0.0, zoomfacy=0.0):
            '''Zoom out the view
               Arguments:
               @zoomfacx (float): in [-inf, inf], (optional)
               @zoomfacy (float): in [-inf, inf], (optional)

            '''

            pass

    class view3d:
        '''Spcecial class, created just to reflect content of bpy.ops.view3d'''

        def background_image_add(name="Image", filepath="", filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Add a new background image (Ctrl for Empty Object)
               Arguments:
               @name (str): Image name to assign
                  (optional, never None)
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @show_multiview (bool): (optional)
               @use_multiview (bool): (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def background_image_remove(index=0):
            '''Remove a background image from the 3D view
               Arguments:
               @index (int): Background image index to remove
                  in [0, inf], (optional)

            '''

            pass

        def camera_to_view():
            '''Set camera view to active view
            '''

            pass

        def camera_to_view_selected():
            '''Move the camera so selected objects are framed
            '''

            pass

        def clear_render_border():
            '''Clear the boundaries of the border render and disable border render
            '''

            pass

        def clip_border(xmin=0, xmax=0, ymin=0, ymax=0):
            '''Set the view clipping border
               Arguments:
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def copybuffer():
            '''Selected objects are saved in a temp file
            '''

            pass

        def cursor3d():
            '''Set the location of the 3D cursor
            '''

            pass

        def dolly(delta=0, mx=0, my=0):
            '''Dolly in/out in the view
               Arguments:
               @delta (int): in [-inf, inf], (optional)
               @mx (int): in [0, inf], (optional)
               @my (int): in [0, inf], (optional)

            '''

            pass

        def edit_mesh_extrude_individual_move():
            '''Extrude individual elements and move
            '''

            pass

        def edit_mesh_extrude_move_normal():
            '''Extrude and move along normals
            '''

            pass

        def edit_mesh_extrude_move_shrink_fatten():
            '''Extrude and move along individual normals
            '''

            pass

        def enable_manipulator(translate=False, rotate=False, scale=False):
            '''Enable the transform manipulator for use
               Arguments:
               @translate (bool): Enable the translate manipulator
                  (optional)
               @rotate (bool): Enable the rotate manipulator
                  (optional)
               @scale (bool): Enable the scale manipulator
                  (optional)

            '''

            pass

        def fly():
            '''Interactively fly around the scene
            '''

            pass

        def game_start():
            '''Start game engine
            '''

            pass

        def layers(nr=1, extend=False, toggle=True):
            '''Toggle layer(s) visibility
               Arguments:
               @nr (int): The layer number to set, zero for all layers
                  in [0, 20], (optional)
               @extend (bool): Add this layer to the current view layers
                  (optional)
               @toggle (bool): Toggle the layer
                  (optional)

            '''

            pass

        def localview():
            '''Toggle display of selected object(s) separately and centered in view
            '''

            pass

        def manipulator(constraint_axis=(False, False, False), constraint_orientation='GLOBAL', release_confirm=False):
            '''Manipulate selected item by axis
               Arguments:
               @constraint_axis (bool): array of 3 items, (optional)
               @constraint_orientation (str): Transformation orientation
                  in [], (optional)
               @release_confirm (bool): Always confirm operation when releasing button
                  (optional)

            '''

            pass

        def manipulator_set(type='TRANSLATE'):
            '''undocumented
               Arguments:
               @type (str): in ['TRANSLATE', 'ROTATE', 'SCALE'], (optional)

            '''

            pass

        def move():
            '''Move the view
            '''

            pass

        def navigate():
            '''Interactively navigate around the scene (uses the mode (walk/fly) preference)
            '''

            pass

        def ndof_all():
            '''Pan and rotate the view with the 3D mouse
            '''

            pass

        def ndof_orbit():
            '''Orbit the view using the 3D mouse
            '''

            pass

        def ndof_orbit_zoom():
            '''Orbit and zoom the view using the 3D mouse
            '''

            pass

        def ndof_pan():
            '''Pan the view with the 3D mouse
            '''

            pass

        def object_as_camera():
            '''Set the active object as the active camera for this view or scene
            '''

            pass

        def pastebuffer(autoselect=True, active_layer=True):
            '''Contents of copy buffer gets pasted
               Arguments:
               @autoselect (bool): Select pasted objects
                  (optional)
               @active_layer (bool): Put pasted objects on the active layer
                  (optional)

            '''

            pass

        def properties():
            '''Toggle the properties region visibility
            '''

            pass

        def render_border(xmin=0, xmax=0, ymin=0, ymax=0, camera_only=False):
            '''Set the boundaries of the border render and enable border render
               Arguments:
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @camera_only (bool): Set render border for camera view and final render only
                  (optional)

            '''

            pass

        def rotate():
            '''Rotate the view
            '''

            pass

        def ruler():
            '''Interactive ruler
            '''

            pass

        def select(extend=False, deselect=False, toggle=False, center=False, enumerate=False, object=False, location=(0, 0)):
            '''Activate/select item(s)
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @deselect (bool): Remove from selection
                  (optional)
               @toggle (bool): Toggle the selection
                  (optional)
               @center (bool): Use the object center when selecting, in editmode used to extend object selection
                  (optional)
               @enumerate (bool): List objects under the mouse (object mode only)
                  (optional)
               @object (bool): Use object selection (editmode only)
                  (optional)
               @location (int): Mouse location
                  array of 2 items in [-inf, inf], (optional)

            '''

            pass

        def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
            '''Select items using border selection
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_circle(x=0, y=0, radius=1, gesture_mode=0):
            '''Select items using circle selection
               Arguments:
               @x (int): in [-inf, inf], (optional)
               @y (int): in [-inf, inf], (optional)
               @radius (int): in [1, inf], (optional)
               @gesture_mode (int): in [-inf, inf], (optional)

            '''

            pass

        def select_lasso(path=None, deselect=False, extend=True):
            '''Select items using lasso selection
               Arguments:
               @path (OperatorMousePath): Collection of , (optional)
               @deselect (bool): Deselect rather than select items
                  (optional)
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_menu(name='', toggle=False):
            '''Menu object selection
               Arguments:
               @name (str): in [], (optional)
               @toggle (bool): Toggle selection instead of deselecting everything first
                  (optional)

            '''

            pass

        def select_or_deselect_all(extend=False, toggle=False, deselect=False, center=False, enumerate=False, object=False):
            '''Select element under the mouse, deselect everything is there's nothing under the mouse
               Arguments:
               @extend (bool): Extend selection instead of deselecting everything first
                  (optional)
               @toggle (bool): Toggle the selection
                  (optional)
               @deselect (bool): Remove from selection
                  (optional)
               @center (bool): Use the object center when selecting, in editmode used to extend object selection
                  (optional)
               @enumerate (bool): List objects under the mouse (object mode only)
                  (optional)
               @object (bool): Use object selection (editmode only)
                  (optional)

            '''

            pass

        def smoothview():
            '''undocumented
            '''

            pass

        def snap_cursor_to_active():
            '''Snap cursor to active item
            '''

            pass

        def snap_cursor_to_center():
            '''Snap cursor to the Center
            '''

            pass

        def snap_cursor_to_grid():
            '''Snap cursor to nearest grid division
            '''

            pass

        def snap_cursor_to_selected():
            '''Snap cursor to center of selected item(s)
            '''

            pass

        def snap_selected_to_active():
            '''Snap selected item(s) to the active item
            '''

            pass

        def snap_selected_to_cursor(use_offset=True):
            '''Snap selected item(s) to cursor
               Arguments:
               @use_offset (bool): (optional)

            '''

            pass

        def snap_selected_to_grid():
            '''Snap selected item(s) to nearest grid division
            '''

            pass

        def toggle_render():
            '''Toggle rendered shading mode of the viewport
            '''

            pass

        def toolshelf():
            '''Toggles tool shelf display
            '''

            pass

        def view_all(use_all_regions=False, center=False):
            '''View all objects in scene
               Arguments:
               @use_all_regions (bool): View selected for all regions
                  (optional)
               @center (bool): (optional)

            '''

            pass

        def view_center_camera():
            '''Center the camera view
            '''

            pass

        def view_center_cursor():
            '''Center the view so that the cursor is in the middle of the view
            '''

            pass

        def view_center_lock():
            '''Center the view lock offset
            '''

            pass

        def view_center_pick():
            '''Center the view to the Z-depth position under the mouse cursor
            '''

            pass

        def view_lock_clear():
            '''Clear all view locking
            '''

            pass

        def view_lock_to_active():
            '''Lock the view to the active object/bone
            '''

            pass

        def view_orbit(angle=0.0, type='ORBITLEFT'):
            '''Orbit the view
               Arguments:
               @angle (float): in [-inf, inf], (optional)
               @type (str): Direction of View Orbit
                  in ['ORBITLEFT', 'ORBITRIGHT', 'ORBITUP', 'ORBITDOWN'], (optional)

            '''

            pass

        def view_pan(type='PANLEFT'):
            '''Pan the view
               Arguments:
               @type (str): Direction of View Pan
                  in ['PANLEFT', 'PANRIGHT', 'PANUP', 'PANDOWN'], (optional)

            '''

            pass

        def view_persportho():
            '''Switch the current view from perspective/orthographic projection
            '''

            pass

        def view_roll(angle=0.0, type='ANGLE'):
            '''Roll the view
               Arguments:
               @angle (float): in [-inf, inf], (optional)
               @type (str): How roll angle is calculated
                  in ['ANGLE', 'LEFT', 'RIGHT'], (optional)

            '''

            pass

        def view_selected(use_all_regions=False):
            '''Move the view to the selection center
               Arguments:
               @use_all_regions (bool): View selected for all regions
                  (optional)

            '''

            pass

        def viewnumpad(type='LEFT', align_active=False):
            '''Use a preset viewpoint
               Arguments:
               @type (str): Preset viewpoint to use
                  in ['LEFT', 'RIGHT', 'BOTTOM', 'TOP', 'FRONT', 'BACK', 'CAMERA'], (optional)
               @align_active (bool): Align to the active object's axis
                  (optional)

            '''

            pass

        def walk():
            '''Interactively walk around the scene
            '''

            pass

        def zoom(delta=0, mx=0, my=0):
            '''Zoom in/out in the view
               Arguments:
               @delta (int): in [-inf, inf], (optional)
               @mx (int): in [0, inf], (optional)
               @my (int): in [0, inf], (optional)

            '''

            pass

        def zoom_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
            '''Zoom in the view to the nearest object contained in the border
               Arguments:
               @gesture_mode (int): in [-inf, inf], (optional)
               @xmin (int): in [-inf, inf], (optional)
               @xmax (int): in [-inf, inf], (optional)
               @ymin (int): in [-inf, inf], (optional)
               @ymax (int): in [-inf, inf], (optional)

            '''

            pass

        def zoom_camera_1_to_1():
            '''Match the camera to 1:1 to the render output
            '''

            pass

    class wm:
        '''Spcecial class, created just to reflect content of bpy.ops.wm'''

        def addon_disable(module=""):
            '''Disable an add-on
               Arguments:
               @module (str): Module name of the add-on to disable
                  (optional, never None)

            '''

            pass

        def addon_enable(module=""):
            '''Enable an add-on
               Arguments:
               @module (str): Module name of the add-on to enable
                  (optional, never None)

            '''

            pass

        def addon_expand(module=""):
            '''Display information and preferences for this add-on
               Arguments:
               @module (str): Module name of the add-on to expand
                  (optional, never None)

            '''

            pass

        def addon_install(overwrite=True, target='DEFAULT', filepath="", filter_folder=True, filter_python=True, filter_glob="*.py;*.zip"):
            '''Install an add-on
               Arguments:
               @overwrite (bool): Remove existing add-ons with the same ID
                  (optional)
               @target (str): in ['DEFAULT', 'PREFS'], (optional)
               @filepath (str): (optional, never None)
               @filter_folder (bool): (optional)
               @filter_python (bool): (optional)
               @filter_glob (str): (optional, never None)

            '''

            pass

        def addon_refresh():
            '''Scan add-on directories for new modules
            '''

            pass

        def addon_remove(module=""):
            '''Delete the add-on from the file system
               Arguments:
               @module (str): Module name of the add-on to remove
                  (optional, never None)

            '''

            pass

        def addon_userpref_show(module=""):
            '''Show add-on user preferences
               Arguments:
               @module (str): Module name of the add-on to expand
                  (optional, never None)

            '''

            pass

        def alembic_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', start=1, end=1, xsamples=1, gsamples=1, sh_open=0.0, sh_close=1.0, selected=False, renderable_only=True, visible_layers_only=False, flatten=False, uvs=True, packuv=True, normals=True, vcolors=False, face_sets=False, subdiv_schema=False, apply_subdiv=False, compression_type='OGAWA', global_scale=1.0):
            '''Export current scene in an Alembic archive
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @start (int): Start Frame
                  in [-inf, inf], (optional)
               @end (int): End Frame
                  in [-inf, inf], (optional)
               @xsamples (int): Number of times per frame transformations are sampled
                  in [1, 128], (optional)
               @gsamples (int): Number of times per frame object data are sampled
                  in [1, 128], (optional)
               @sh_open (float): Time at which the shutter is open
                  in [-1, 1], (optional)
               @sh_close (float): Time at which the shutter is closed
                  in [-1, 1], (optional)
               @selected (bool): Export only selected objects
                  (optional)
               @renderable_only (bool): Export only objects marked renderable in the outliner
                  (optional)
               @visible_layers_only (bool): Export only objects in visible layers
                  (optional)
               @flatten (bool): Do not preserve objects' parent/children relationship
                  (optional)
               @uvs (bool): Export UVs
                  (optional)
               @packuv (bool): Export UVs with packed island
                  (optional)
               @normals (bool): Export normals
                  (optional)
               @vcolors (bool): Export vertex colors
                  (optional)
               @face_sets (bool): Export per face shading group assignments
                  (optional)
               @subdiv_schema (bool): Export meshes using Alembic's subdivision schema
                  (optional)
               @apply_subdiv (bool): Export subdivision surfaces as meshes
                  (optional)
               @compression_type (str): in ['OGAWA', 'HDF5'], (optional)
               @global_scale (float): Value by which to enlarge or shrink the objects with respect to the world's origin
                  in [0.0001, 1000], (optional)

            '''

            pass

        def alembic_import(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', scale=1.0, set_frame_range=True, validate_meshes=False, is_sequence=False):
            '''Load an Alembic archive
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @scale (float): Value by which to enlarge or shrink the objects with respect to the world's origin
                  in [0.0001, 1000], (optional)
               @set_frame_range (bool): If checked, update scene's start and end frame to match those of the Alembic archive
                  (optional)
               @validate_meshes (bool): Check imported mesh objects for invalid data (slow)
                  (optional)
               @is_sequence (bool): Set to true if the cache is split into separate files
                  (optional)

            '''

            pass

        def appconfig_activate(filepath=""):
            '''undocumented
               Arguments:
               @filepath (str): (optional, never None)

            '''

            pass

        def appconfig_default():
            '''undocumented
            '''

            pass

        def append(filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=True, filemode=1, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', link=False, autoselect=True, active_layer=True, instance_groups=False, set_fake=False, use_recursive=True):
            '''Append from a Library .blend file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @directory (str): Directory of the file
                  (optional, never None)
               @filename (str): Name of the file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @link (bool): Link the objects or datablocks rather than appending
                  (optional)
               @autoselect (bool): Select new objects
                  (optional)
               @active_layer (bool): Put new objects on the active layer
                  (optional)
               @instance_groups (bool): Create Dupli-Group instances for each group
                  (optional)
               @set_fake (bool): Set Fake User for appended items (except Objects and Groups)
                  (optional)
               @use_recursive (bool): Localize all appended data, including those indirectly linked from other libraries
                  (optional)

            '''

            pass

        def blenderplayer_start():
            '''Launch the blender-player with the current blend-file
            '''

            pass

        def call_menu(name=""):
            '''Call (draw) a pre-defined menu
               Arguments:
               @name (str): Name of the menu
                  (optional, never None)

            '''

            pass

        def call_menu_pie(name=""):
            '''Call (draw) a pre-defined pie menu
               Arguments:
               @name (str): Name of the pie menu
                  (optional, never None)

            '''

            pass

        def collada_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', apply_modifiers=False, export_mesh_type=0, export_mesh_type_selection='view', selected=False, include_children=False, include_armatures=False, include_shapekeys=True, deform_bones_only=False, active_uv_only=False, include_uv_textures=False, include_material_textures=False, use_texture_copies=True, triangulate=True, use_object_instantiation=True, use_blender_profile=True, sort_by_name=False, export_transformation_type=0, export_transformation_type_selection='matrix', open_sim=False):
            '''Save a Collada file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @apply_modifiers (bool): Apply modifiers to exported mesh (non destructive))
                  (optional)
               @export_mesh_type (int): Modifier resolution for export
                  in [-inf, inf], (optional)
               @export_mesh_type_selection (str): Modifier resolution for export
                  in ['view', 'render'], (optional)
               @selected (bool): Export only selected elements
                  (optional)
               @include_children (bool): Export all children of selected objects (even if not selected)
                  (optional)
               @include_armatures (bool): Export related armatures (even if not selected)
                  (optional)
               @include_shapekeys (bool): Export all Shape Keys from Mesh Objects
                  (optional)
               @deform_bones_only (bool): Only export deforming bones with armatures
                  (optional)
               @active_uv_only (bool): Export only the selected UV Map
                  (optional)
               @include_uv_textures (bool): Export textures assigned to the object UV Maps
                  (optional)
               @include_material_textures (bool): Export textures assigned to the object Materials
                  (optional)
               @use_texture_copies (bool): Copy textures to same folder where the .dae file is exported
                  (optional)
               @triangulate (bool): Export Polygons (Quads & NGons) as Triangles
                  (optional)
               @use_object_instantiation (bool): Instantiate multiple Objects from same Data
                  (optional)
               @use_blender_profile (bool): Export additional Blender specific information (for material, shaders, bones, etc.)
                  (optional)
               @sort_by_name (bool): Sort exported data by Object name
                  (optional)
               @export_transformation_type (int): Transformation type for translation, scale and rotation
                  in [-inf, inf], (optional)
               @export_transformation_type_selection (str): Transformation type for translation, scale and rotation
                  in ['matrix', 'transrotloc', 'both'], (optional)
               @open_sim (bool): Compatibility mode for SL, OpenSim and other compatible online worlds
                  (optional)

            '''

            pass

        def collada_import(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', import_units=False, fix_orientation=False, find_chains=False, auto_connect=False, min_chain_length=0):
            '''Load a Collada file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @import_units (bool): If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene
                  (optional)
               @fix_orientation (bool): Fix Orientation of Leaf Bones (Collada does only support Joints)
                  (optional)
               @find_chains (bool): Find best matching Bone Chains and ensure bones in chain are connected
                  (optional)
               @auto_connect (bool): Set use_connect for parent bones which have exactly one child bone
                  (optional)
               @min_chain_length (int): When searching Bone Chains disregard chains of length below this value
                  in [0, inf], (optional)

            '''

            pass

        def console_toggle():
            '''Toggle System Console
            '''

            pass

        def context_collection_boolean_set(data_path_iter="", data_path_item="", type='TOGGLE'):
            '''Set boolean values for a collection of items
               Arguments:
               @data_path_iter (str): The data path relative to the context, must point to an iterable
                  (optional, never None)
               @data_path_item (str): The data path from each iterable to the value (int or float)
                  (optional, never None)
               @type (str): in ['TOGGLE', 'ENABLE', 'DISABLE'], (optional)

            '''

            pass

        def context_cycle_array(data_path="", reverse=False):
            '''Set a context array value (useful for cycling the active mesh edit mode)
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @reverse (bool): Cycle backwards
                  (optional)

            '''

            pass

        def context_cycle_enum(data_path="", reverse=False, wrap=False):
            '''Toggle a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @reverse (bool): Cycle backwards
                  (optional)
               @wrap (bool): Wrap back to the first/last values
                  (optional)

            '''

            pass

        def context_cycle_int(data_path="", reverse=False, wrap=False):
            '''Set a context value (useful for cycling active material, vertex keys, groups, etc.)
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @reverse (bool): Cycle backwards
                  (optional)
               @wrap (bool): Wrap back to the first/last values
                  (optional)

            '''

            pass

        def context_menu_enum(data_path=""):
            '''undocumented
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)

            '''

            pass

        def context_modal_mouse(data_path_iter="", data_path_item="", header_text="", input_scale=0.01, invert=False, initial_x=0):
            '''Adjust arbitrary values with mouse input
               Arguments:
               @data_path_iter (str): The data path relative to the context, must point to an iterable
                  (optional, never None)
               @data_path_item (str): The data path from each iterable to the value (int or float)
                  (optional, never None)
               @header_text (str): Text to display in header during scale
                  (optional, never None)
               @input_scale (float): Scale the mouse movement by this value before applying the delta
                  in [-inf, inf], (optional)
               @invert (bool): Invert the mouse input
                  (optional)
               @initial_x (int): in [-inf, inf], (optional)

            '''

            pass

        def context_pie_enum(data_path=""):
            '''undocumented
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)

            '''

            pass

        def context_scale_float(data_path="", value=1.0):
            '''Scale a float context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (float): Assign value
                  in [-inf, inf], (optional)

            '''

            pass

        def context_scale_int(data_path="", value=1.0, always_step=True):
            '''Scale an int context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (float): Assign value
                  in [-inf, inf], (optional)
               @always_step (bool): Always adjust the value by a minimum of 1 when 'value' is not 1.0
                  (optional)

            '''

            pass

        def context_set_boolean(data_path="", value=True):
            '''Set a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (bool): Assignment value
                  (optional)

            '''

            pass

        def context_set_enum(data_path="", value=""):
            '''Set a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (str): Assignment value (as a string)
                  (optional, never None)

            '''

            pass

        def context_set_float(data_path="", value=0.0, relative=False):
            '''Set a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (float): Assignment value
                  in [-inf, inf], (optional)
               @relative (bool): Apply relative to the current value (delta)
                  (optional)

            '''

            pass

        def context_set_id(data_path="", value=""):
            '''Set a context value to an ID data-block
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (str): Assign value
                  (optional, never None)

            '''

            pass

        def context_set_int(data_path="", value=0, relative=False):
            '''Set a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (int): Assign value
                  in [-inf, inf], (optional)
               @relative (bool): Apply relative to the current value (delta)
                  (optional)

            '''

            pass

        def context_set_string(data_path="", value=""):
            '''Set a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (str): Assign value
                  (optional, never None)

            '''

            pass

        def context_set_value(data_path="", value=""):
            '''Set a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value (str): Assignment value (as a string)
                  (optional, never None)

            '''

            pass

        def context_toggle(data_path=""):
            '''Toggle a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)

            '''

            pass

        def context_toggle_enum(data_path="", value_1="", value_2=""):
            '''Toggle a context value
               Arguments:
               @data_path (str): RNA context string
                  (optional, never None)
               @value_1 (str): Toggle enum
                  (optional, never None)
               @value_2 (str): Toggle enum
                  (optional, never None)

            '''

            pass

        def copy_prev_settings():
            '''Copy settings from previous version
            '''

            pass

        def debug_menu(debug_value=0):
            '''Open a popup to set the debug level
               Arguments:
               @debug_value (int): in [-32768, 32767], (optional)

            '''

            pass

        def dependency_relations():
            '''Print dependency graph relations to the console
            '''

            pass

        def doc_view(doc_id=""):
            '''Load online reference docs
               Arguments:
               @doc_id (str): (optional, never None)

            '''

            pass

        def doc_view_manual(doc_id=""):
            '''Load online manual
               Arguments:
               @doc_id (str): (optional, never None)

            '''

            pass

        def doc_view_manual_ui_context():
            '''View a context based online manual in a web browser
            '''

            pass

        def interaction_preset_add(name="", remove_active=False):
            '''Add or remove an Application Interaction Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def interface_theme_preset_add(name="", remove_active=False):
            '''Add or remove a theme preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def keyconfig_activate(filepath=""):
            '''undocumented
               Arguments:
               @filepath (str): (optional, never None)

            '''

            pass

        def keyconfig_export(filepath="keymap.py", filter_folder=True, filter_text=True, filter_python=True):
            '''Export key configuration to a python script
               Arguments:
               @filepath (str): (optional, never None)
               @filter_folder (bool): (optional)
               @filter_text (bool): (optional)
               @filter_python (bool): (optional)

            '''

            pass

        def keyconfig_import(filepath="keymap.py", filter_folder=True, filter_text=True, filter_python=True, keep_original=True):
            '''Import key configuration from a python script
               Arguments:
               @filepath (str): (optional, never None)
               @filter_folder (bool): (optional)
               @filter_text (bool): (optional)
               @filter_python (bool): (optional)
               @keep_original (bool): Keep original file after copying to configuration folder
                  (optional)

            '''

            pass

        def keyconfig_preset_add(name="", remove_active=False):
            '''Add or remove a Key-config Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)

            '''

            pass

        def keyconfig_remove():
            '''Remove key config
            '''

            pass

        def keyconfig_test():
            '''Test key-config for conflicts
            '''

            pass

        def keyitem_add():
            '''Add key map item
            '''

            pass

        def keyitem_remove(item_id=0):
            '''Remove key map item
               Arguments:
               @item_id (int): Identifier of the item to remove
                  in [-inf, inf], (optional)

            '''

            pass

        def keyitem_restore(item_id=0):
            '''Restore key map item
               Arguments:
               @item_id (int): Identifier of the item to remove
                  in [-inf, inf], (optional)

            '''

            pass

        def keymap_restore(all=False):
            '''Restore key map(s)
               Arguments:
               @all (bool): Restore all keymaps to default
                  (optional)

            '''

            pass

        def lib_reload(library="", filepath="", directory="", filename="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Reload the given library
               Arguments:
               @library (str): Library to reload
                  (optional, never None)
               @filepath (str): Path to file
                  (optional, never None)
               @directory (str): Directory of the file
                  (optional, never None)
               @filename (str): Name of the file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def lib_relocate(library="", filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
            '''Relocate the given library to one or several others
               Arguments:
               @library (str): Library to relocate
                  (optional, never None)
               @filepath (str): Path to file
                  (optional, never None)
               @directory (str): Directory of the file
                  (optional, never None)
               @filename (str): Name of the file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def link(filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=True, filemode=1, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', link=True, autoselect=True, active_layer=True, instance_groups=True):
            '''Link from a Library .blend file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @directory (str): Directory of the file
                  (optional, never None)
               @filename (str): Name of the file
                  (optional, never None)
               @files (OperatorFileListElement): Collection of , (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @relative_path (bool): Select the file relative to the blend file
                  (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @link (bool): Link the objects or datablocks rather than appending
                  (optional)
               @autoselect (bool): Select new objects
                  (optional)
               @active_layer (bool): Put new objects on the active layer
                  (optional)
               @instance_groups (bool): Create Dupli-Group instances for each group
                  (optional)

            '''

            pass

        def memory_statistics():
            '''Print memory statistics to the console
            '''

            pass

        def open_mainfile(filepath="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', load_ui=True, use_scripts=True):
            '''Open a Blender file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @load_ui (bool): Load user interface setup in the .blend file
                  (optional)
               @use_scripts (bool): Allow .blend file to execute scripts automatically, default available from system preferences
                  (optional)

            '''

            pass

        def operator_cheat_sheet():
            '''undocumented
            '''

            pass

        def operator_defaults():
            '''Set the active operator to its default values
            '''

            pass

        def operator_pie_enum(data_path="", prop_string=""):
            '''undocumented
               Arguments:
               @data_path (str): Operator name (in python as string)
                  (optional, never None)
               @prop_string (str): Property name (as a string)
                  (optional, never None)

            '''

            pass

        def operator_preset_add(name="", remove_active=False, operator=""):
            '''Add or remove an Operator Preset
               Arguments:
               @name (str): Name of the preset, used to make the path name
                  (optional, never None)
               @remove_active (bool): (optional)
               @operator (str): (optional, never None)

            '''

            pass

        def path_open(filepath=""):
            '''Open a path in a file browser
               Arguments:
               @filepath (str): (optional, never None)

            '''

            pass

        def previews_batch_clear(files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_groups=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True):
            '''Clear selected .blend file's previews
               Arguments:
               @files (OperatorFileListElement): Collection of , (optional)
               @directory (str): (optional, never None)
               @filter_blender (bool): (optional)
               @filter_folder (bool): (optional)
               @use_scenes (bool): Clear scenes' previews
                  (optional)
               @use_groups (bool): Clear groups' previews
                  (optional)
               @use_objects (bool): Clear objects' previews
                  (optional)
               @use_intern_data (bool): Clear 'internal' previews (materials, textures, images, etc.)
                  (optional)
               @use_trusted (bool): Enable python evaluation for selected files
                  (optional)
               @use_backups (bool): Keep a backup (.blend1) version of the files when saving with cleared previews
                  (optional)

            '''

            pass

        def previews_batch_generate(files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_groups=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True):
            '''Generate selected .blend file's previews
               Arguments:
               @files (OperatorFileListElement): Collection of , (optional)
               @directory (str): (optional, never None)
               @filter_blender (bool): (optional)
               @filter_folder (bool): (optional)
               @use_scenes (bool): Generate scenes' previews
                  (optional)
               @use_groups (bool): Generate groups' previews
                  (optional)
               @use_objects (bool): Generate objects' previews
                  (optional)
               @use_intern_data (bool): Generate 'internal' previews (materials, textures, images, etc.)
                  (optional)
               @use_trusted (bool): Enable python evaluation for selected files
                  (optional)
               @use_backups (bool): Keep a backup (.blend1) version of the files when saving with generated previews
                  (optional)

            '''

            pass

        def previews_clear(id_type={'GROUP', 'IMAGE', 'LAMP', 'MATERIAL', 'OBJECT', 'SCENE', 'TEXTURE', 'WORLD'}):
            '''Clear datablock previews (only for some types like objects, materials, textures, etc.)
               Arguments:
               @id_type (str): Which datablock previews to clear
                  set in {'SCENE', 'GROUP', 'OBJECT', 'MATERIAL', 'LAMP', 'WORLD', 'TEXTURE', 'IMAGE'}, (optional)

            '''

            pass

        def previews_ensure():
            '''Ensure datablock previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)
            '''

            pass

        def properties_add(data_path=""):
            '''undocumented
               Arguments:
               @data_path (str): Property data_path edit
                  (optional, never None)

            '''

            pass

        def properties_context_change(context=""):
            '''Jump to a different tab inside the properties editor
               Arguments:
               @context (str): (optional, never None)

            '''

            pass

        def properties_edit(data_path="", property="", value="", min=-10000, max=10000.0, use_soft_limits=False, soft_min=-10000, soft_max=10000.0, description=""):
            '''undocumented
               Arguments:
               @data_path (str): Property data_path edit
                  (optional, never None)
               @property (str): Property name edit
                  (optional, never None)
               @value (str): Property value edit
                  (optional, never None)
               @min (float): in [-inf, inf], (optional)
               @max (float): in [-inf, inf], (optional)
               @use_soft_limits (bool): (optional)
               @soft_min (float): in [-inf, inf], (optional)
               @soft_max (float): in [-inf, inf], (optional)
               @description (str): (optional, never None)

            '''

            pass

        def properties_remove(data_path="", property=""):
            '''Internal use (edit a property data_path)
               Arguments:
               @data_path (str): Property data_path edit
                  (optional, never None)
               @property (str): Property name edit
                  (optional, never None)

            '''

            pass

        def quit_blender():
            '''Quit Blender
            '''

            pass

        def radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False):
            '''Set some size property (like e.g. brush size) with mouse wheel
               Arguments:
               @data_path_primary (str): Primary path of property to be set by the radial control
                  (optional, never None)
               @data_path_secondary (str): Secondary path of property to be set by the radial control
                  (optional, never None)
               @use_secondary (str): Path of property to select between the primary and secondary data paths
                  (optional, never None)
               @rotation_path (str): Path of property used to rotate the texture display
                  (optional, never None)
               @color_path (str): Path of property used to set the color of the control
                  (optional, never None)
               @fill_color_path (str): Path of property used to set the fill color of the control
                  (optional, never None)
               @fill_color_override_path (str): (optional, never None)
               @fill_color_override_test_path (str): (optional, never None)
               @zoom_path (str): Path of property used to set the zoom level for the control
                  (optional, never None)
               @image_id (str): Path of ID that is used to generate an image for the control
                  (optional, never None)
               @secondary_tex (bool): Tweak brush secondary/mask texture
                  (optional)

            '''

            pass

        def read_factory_settings():
            '''Load default file and user preferences
            '''

            pass

        def read_history():
            '''Reloads history and bookmarks
            '''

            pass

        def read_homefile(filepath="", load_ui=True):
            '''Open the default file (doesn't save the current file)
               Arguments:
               @filepath (str): Path to an alternative start-up file
                  (optional, never None)
               @load_ui (bool): Load user interface setup from the .blend file
                  (optional)

            '''

            pass

        def recover_auto_save(filepath="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=False, filter_blenlib=False, filemode=8, display_type='LIST_LONG', sort_method='FILE_SORT_TIME'):
            '''Open an automatically saved file to recover it
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

            '''

            pass

        def recover_last_session():
            '''Open the last closed file ("quit.blend")
            '''

            pass

        def redraw_timer(type='DRAW', iterations=10, time_limit=0.0):
            '''Simple redraw timer to test the speed of updating the interface
               Arguments:
               @type (str): in ['DRAW', 'DRAW_SWAP', 'DRAW_WIN', 'DRAW_WIN_SWAP', 'ANIM_STEP', 'ANIM_PLAY', 'UNDO'], (optional)
               @iterations (int): Number of times to redraw
                  in [1, inf], (optional)
               @time_limit (float): Seconds to run the test for (override iterations)
                  in [0, inf], (optional)

            '''

            pass

        def revert_mainfile(use_scripts=True):
            '''Reload the saved file
               Arguments:
               @use_scripts (bool): Allow .blend file to execute scripts automatically, default available from system preferences
                  (optional)

            '''

            pass

        def save_as_mainfile(filepath="", check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', compress=False, relative_remap=True, copy=False, use_mesh_compat=False):
            '''Save the current file in the desired location
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @compress (bool): Write compressed .blend file
                  (optional)
               @relative_remap (bool): Remap relative paths when saving in a different directory
                  (optional)
               @copy (bool): Save a copy of the actual working state but does not make saved file active
                  (optional)
               @use_mesh_compat (bool): Save using legacy mesh format (no ngons) - WARNING: only saves tris and quads, other ngons will be lost (no implicit triangulation)
                  (optional)

            '''

            pass

        def save_homefile():
            '''Make the current file the default .blend file, includes preferences
            '''

            pass

        def save_mainfile(filepath="", check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', compress=False, relative_remap=False):
            '''Save the current Blender file
               Arguments:
               @filepath (str): Path to file
                  (optional, never None)
               @check_existing (bool): Check and warn on overwriting existing files
                  (optional)
               @filter_blender (bool): (optional)
               @filter_backup (bool): (optional)
               @filter_image (bool): (optional)
               @filter_movie (bool): (optional)
               @filter_python (bool): (optional)
               @filter_font (bool): (optional)
               @filter_sound (bool): (optional)
               @filter_text (bool): (optional)
               @filter_btx (bool): (optional)
               @filter_collada (bool): (optional)
               @filter_alembic (bool): (optional)
               @filter_folder (bool): (optional)
               @filter_blenlib (bool): (optional)
               @filemode (int): The setting for the file browser mode to load a .blend file, a library or a special file
                  in [1, 9], (optional)
               @display_type (str): in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
               @sort_method (str): in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
               @compress (bool): Write compressed .blend file
                  (optional)
               @relative_remap (bool): Remap relative paths when saving in a different directory
                  (optional)

            '''

            pass

        def save_userpref():
            '''Save user preferences separately, overrides startup file preferences
            '''

            pass

        def search_menu():
            '''Pop-up a search menu over all available operators in current context
            '''

            pass

        def set_stereo_3d(display_mode='ANAGLYPH', anaglyph_type='RED_CYAN', interlace_type='ROW_INTERLEAVED', use_interlace_swap=False, use_sidebyside_crosseyed=False):
            '''Toggle 3D stereo support for current window (or change the display mode)
               Arguments:
               @display_mode (str): in ['ANAGLYPH', 'INTERLACE', 'TIMESEQUENTIAL', 'SIDEBYSIDE', 'TOPBOTTOM'], (optional)
               @anaglyph_type (str): in ['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE'], (optional)
               @interlace_type (str): in ['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED'], (optional)
               @use_interlace_swap (bool): Swap left and right stereo channels
                  (optional)
               @use_sidebyside_crosseyed (bool): Right eye should see left image and vice-versa
                  (optional)

            '''

            pass

        def splash():
            '''Open the splash screen with release info
            '''

            pass

        def sysinfo(filepath=""):
            '''Generate system information, saved into a text file
               Arguments:
               @filepath (str): (optional, never None)

            '''

            pass

        def theme_install(overwrite=True, filepath="", filter_folder=True, filter_glob="*.xml"):
            '''Load and apply a Blender XML theme file
               Arguments:
               @overwrite (bool): Remove existing theme file if exists
                  (optional)
               @filepath (str): (optional, never None)
               @filter_folder (bool): (optional)
               @filter_glob (str): (optional, never None)

            '''

            pass

        def url_open(url=""):
            '''Open a website in the web-browser
               Arguments:
               @url (str): URL to open
                  (optional, never None)

            '''

            pass

        def userpref_autoexec_path_add():
            '''Add path to exclude from autoexecution
            '''

            pass

        def userpref_autoexec_path_remove(index=0):
            '''Remove path to exclude from autoexecution
               Arguments:
               @index (int): in [0, inf], (optional)

            '''

            pass

        def window_close():
            '''Close the current Blender window
            '''

            pass

        def window_duplicate():
            '''Duplicate the current Blender window
            '''

            pass

        def window_fullscreen_toggle():
            '''Toggle the current window fullscreen
            '''

            pass

    class world:
        '''Spcecial class, created just to reflect content of bpy.ops.world'''

        def new():
            '''Add a new world
            '''

            pass
